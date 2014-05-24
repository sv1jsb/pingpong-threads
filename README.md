pingpong-threads
================

Python threading project. Play pingpong with threads.

This is a python port of [Dr. Douglas C. Schmidt](http://www.dre.vanderbilt.edu/~schmidt/)'s example project [Pingpong](https://github.com/douglascraigschmidt/POSA-14/tree/master/ex/PingPong).
It's an example of using and synchronizing threads in java, as part of coursera's [POSA-002](https://www.coursera.org/course/posa) MOOC.

### Python port specifics

#### Threads
This python port uses Semaphores, RLocks and Conditions to synchronize threads. Also an implementation of java's CountDownLatch is used to enforce a barrier synchronization of the two threads.

#### Pattterns
As the original project, the python port uses the Template pattern to instantiate concrete ping and pong threads, and the Strategy pattern to provide environment specific output and control.

