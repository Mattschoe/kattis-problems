#!/usr/bin/env python3
import random
import sys

def random_floor() -> int:
    """
    Returns a random floor
    """
    return random.randint(1, 5)

def min_group_random_floor():
    """
    S = 1
    F = random
    Should be the worst case <for implementation, since (atleast for my implementation)
    would have to walk back 50 positions before capacity runs out.
    """
    N = 200_000
    C = 50
    print(N, C)
    for _ in range(N):
        print(1, random_floor())

def min_group_max_floor():
    """
    S = 1
    F = 5
    A good sanity checker for implementation since this has to give
    43_995 (per trip: 5 (up) + 1 (stop) + 5 (down), except for last.
    4_000 trip totals = 43_995.
    """
    N = 200_000
    C = 50
    print(N, C)
    for _ in range(N):
        print(1, 5)

def min_capacity_max_groups():
    N = 200_000
    C = 1
    print(N, C)
    for _ in range(N):
        print(1, random_floor())

min_capacity_max_groups()