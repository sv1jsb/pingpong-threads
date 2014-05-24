# -*- coding: utf-8 -*-
"""
Ping pong wiht threads.
Uses Semaphores, RLocks and Conditions.
"""
from threading import Semaphore, RLock, Condition
from platformstrategy import ConsoleStrategy
from pingpongthreads import PingPongThreadSema, PingPongThreadCond

__all__ = ['PingPong']


class PingPong(object):
    """
    PingPong class.
    Creates two threads to play ping pong.
    """

    def __init__(self, strg='CON', sync='SEMA', iters=10, turns=5):
        """
        Named parameters:
        strg:   the strategy to use, defaults to console
        sync:   the synching mechanism, defaults to semaphores
        iters:  number of iterations to perform
        turns:  number of turns when synching mechanism is conditions
        """
        if strg == 'CON':
            self.strategy = ConsoleStrategy()
        else:
            raise Exception("Not yet implemented")
        if sync == 'SEMA':
            pingsema = Semaphore(1)
            pongsema = Semaphore(0)
            self.ping = PingPongThreadSema('ping', pingsema, pongsema, iters, self.strategy)
            self.pong = PingPongThreadSema('pong', pongsema, pingsema, iters, self.strategy)
        else:
            rlock = RLock()
            pingcond = Condition(rlock)
            pongcond = Condition(rlock)
            self.pong = PingPongThreadCond('pong', rlock, pongcond, pingcond, False, iters, turns, self.strategy)
            self.ping = PingPongThreadCond('ping', rlock, pingcond, pongcond, True, iters, turns, self.strategy)
            self.ping.set_other_thread_id(self.pong.__hash__())
            self.pong.set_other_thread_id(self.ping.__hash__())

    def play(self):
        """
        Play ping pong with threads.
        """
        self.strategy.strg_prnt("Ready... Set... Go...")
        self.strategy.begin()
        self.ping.start()
        self.pong.start()
        self.strategy.await_done()
        self.strategy.strg_prnt("Done!")