# -*- coding: utf-8 -*-
"""
Type of main threads of ping pong
"""
from threading import Thread


class PingPongThread(Thread):
    """
    Base class for ping pong threads.
    """
    owner = ""

    def __init__(self, outstring, iters, strategy):
        """
        outstring:  the string to print
        iters:      the number of iterations
        strategy:   the strategy to use
        """
        Thread.__init__(self)
        self.outstring = outstring
        self.iters = iters
        self.other_thread_id = None
        self.strategy = strategy

    def set_other_thread_id(self, other_id):
        """
        Implemented by subclass
        """
        pass

    def acquire(self):
        """
        Implemented by subclass
        """
        pass

    def release(self):
        """
        Implemented by subclass
        """
        pass

    def run(self):
        """
        Loop self.iters times.
        When done inform thread has finished
        """
        for i in range(self.iters):
            self.acquire()
            self.strategy.strg_prnt("%s (%d)" % (self.outstring, i+1))
            self.release()
        self.strategy.done()


class PingPongThreadSema(PingPongThread):
    """
    Thread using semaphores.
    """
    FIRST_SEMA = 0
    SECOND_SEMA = 1

    def __init__(self, outstring, firstsema, secondsema, mi, sp):
        self.semas = [None, None]
        PingPongThread.__init__(self, outstring, mi, sp)
        self.semas[PingPongThreadSema.FIRST_SEMA] = firstsema
        self.semas[PingPongThreadSema.SECOND_SEMA] = secondsema

    def acquire(self):
        """
        Running thread acquires semaphore
        """
        self.semas[PingPongThreadSema.FIRST_SEMA].acquire()

    def release(self):
        """
        Running thread is going to sleep. Wake up the other thread
        """
        self.semas[PingPongThreadSema.SECOND_SEMA].release()


class PingPongThreadCond(PingPongThread):
    """
    Thread using conditions.
    """
    FIRST_COND = 0
    SECOND_COND = 1

    def __init__(self, outstring, lock, first_cond, second_cond, own, mi, turns, sp):
        self.conds = [None, None]
        PingPongThread.__init__(self, outstring, mi, sp)
        self.lock = lock
        self.conds[PingPongThreadCond.FIRST_COND] = first_cond
        self.conds[PingPongThreadCond.SECOND_COND] = second_cond
        self.turns = turns
        self.countdown = turns
        if own:
            PingPongThreadCond.owner = self.__hash__()
        else:
            PingPongThreadCond.owner = ""

    def acquire(self):
        """
        Thread waits for control
        """
        self.lock.acquire()
        endless = True
        while endless and PingPongThreadCond.owner != self.__hash__():
            endless = self.conds[PingPongThreadCond.FIRST_COND].wait(3)
        self.lock.release()

    def release(self):
        """
        Thread with control runs for 'turns' times
        """
        self.lock.acquire()
        self.countdown -= 1
        if self.countdown == 0:
            PingPongThreadCond.owner = self.other_thread_id
            self.countdown = self.turns
            self.conds[PingPongThreadCond.SECOND_COND].notify()
        self.lock.release()

    def set_other_thread_id(self, other_id):
        """
        Sets other thread's id
        """
        self.other_thread_id = other_id