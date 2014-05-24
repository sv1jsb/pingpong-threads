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
    Strategy for console output
    """
    def strg_prnt(self, outstr):
        """
        Outputs to standard out
        """
        return sys.stdout.write("%s\n" % outstr)
