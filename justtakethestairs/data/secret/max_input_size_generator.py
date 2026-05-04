#!/usr/bin/env python3
import random
import sys

N = 200_000
C = 50

def min_group_random_floor():
    """
    S = 1
    F = random
    Should be the worst case <for implementation, since (atleast for my implementation)
    would have to walk back 50 positions before capacity runs out.
    """
    print(N, C)
    for _ in range(N):
        print(1, random.randint(1, 5))

def min_group_max_floor():
    """
    S = 1
    F = 5
    A good sanity checker for implementation since this has to give
    43_995 (per trip: 5 (up) + 1 (stop) + 5 (down), except for last.
    4_000 trip totals = 43_995.
    """
    print(N, C)
    for _ in range(N):
        print(1, 5)