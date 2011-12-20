#!/usr/bin/python2

# This program is Free Software under the terms of
# the Do What The Fuck You Want To Public License (WTFPL)
# See wtfpl.txt or http://sam.zoy.org/wtfpl/COPYING
# for a copy of the license.

# Provides a tictoc function that can be used to measure performance of
# a function, either once or as average over n runs.

import time
import sys

def tictoc(func, args, n = 1):
    '''Get the runtime of a function, averaged over n runs.

    Arguments:
        func -- a function object
        args -- a tuple containing the arguments for func
        n -- amount of times to run func
        
    Returns:
        A float representing the average runtime.
    '''
    tic = time.time()
    for _ in range(0, n):
        func(*args)
    toc = time.time() - tic
    return toc / n

