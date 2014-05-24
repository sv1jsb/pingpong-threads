pingpong-threads
================

Python threading project. Play pingpong with threads.

This is a python port of [Dr. Douglas C. Schmidt](http://www.dre.vanderbilt.edu/~schmidt/)'s example project [Pingpong](https://github.com/douglascraigschmidt/POSA-14/tree/master/ex/PingPong).
It's an example of using and synchronizing threads in java, as part of coursera's [POSA-002](https://www.coursera.org/course/posa) MOOC.

### Python port specifics

#### Threads
This python port uses Semaphores, RLocks and Conditions to synchronize threads. Also an implementation of java's CountDownLatch is used to enforce a barrier synchronization of the two threads.

#### Pattterns
As the original project, the python port uses the Template pattern to instantiate concrete ping and pong threads, and the Strategy pattern to provide environment specific output and control. The Singleton pattern is used for providing only one object for a Strategy class.


### Use

All code is in pingpong directory. The program is designed so it can be run by command prompt or be imported as a module.
In both uses, if no arguments are given it will run with the default values.

Run:

    python pp.py -h

at the toplevel directory of this repository for help on command arguments. The same ones are expected when imported as a module.

### Have fun
Clone and experiment. After all this is an educational project. 




