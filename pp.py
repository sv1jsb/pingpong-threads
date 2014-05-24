# -*- coding: utf-8 -*-
"""
Run Pipng pong threads game from console
"""
import argparse
from pingpong import PingPong

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play ping pong with threads')
    parser.add_argument('-i', default=10, help='iterations to perform, defaults to 10', type=int, dest='iters')
    parser.add_argument('-s', default='CON', help='strategy to use, defaults to console', choices=['CON', 'WIN'],
                        dest='strg')
    parser.add_argument('-m', default='SEMA', choices=['SEMA', 'COND'], help='sync mechanism, defaults to semaphores',
                        dest='sync')
    parser.add_argument('-t', default=5, help='number of turns if sync mechanism is COND, defaults to 5', type=int,
                        dest='turns')
    pp = PingPong(**vars(parser.parse_args()))
    pp.play()
