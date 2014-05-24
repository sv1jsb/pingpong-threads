# -*- coding: utf-8 -*-
"""
Strategies to use for control and output
"""
import sys
from utils import CountDownLatch


class Strategy(object):
    """
    Base class for strategy used
    """
    latch = None

    @staticmethod
    def begin():
        """
        Use countdown latch to control threads
        """
        Strategy.latch = CountDownLatch(2)

    @staticmethod
    def done():
        """
        When thread is done decrement latch
        """
        Strategy.latch.count_down()

    @staticmethod
    def await_done():
        """
        Wait till all threads are done.
        """
        Strategy.latch.await()

    def strg_prnt(self, outstr):
        """
        The function to use for output
        """
        pass


class ConsoleStrategy(Strategy):
    """
    Strategy for console output.
    Implements the Singleton pattern.
    """
    def __new__(cls):
        if not hasattr(cls, '_inst'):
            cls._inst = super(ConsoleStrategy, cls).__new__(cls)
        return cls._inst

    def strg_prnt(self, outstr):
        """
        Outputs to standard out
        """
        return sys.stdout.write("%s\n" % outstr)
