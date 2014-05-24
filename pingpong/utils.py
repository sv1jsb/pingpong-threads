# -*- coding: utf-8 -*-
"""
Python implementation of java's CountDownLatch
"""
from threading import Condition


class CountDownLatch(object):
    """
    Implements java's CountDownLatch
    count: number of countdowns
    """
    def __init__(self, count=1):
        self.count = count
        self.lock = Condition()

    def count_down(self):
        """
        Decrease count by one.
        When zero is reached notify all threads
        """
        with self.lock:
            self.count -= 1

            if self.count <= 0:
                self.lock.notifyAll()

    def await(self):
        """
        Wait for latch to reach zero
        """
        with self.lock:
            while self.count > 0:
                self.lock.wait()