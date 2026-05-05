#The basic idea of the brute force solution is:
#"Try every possible way to split the groups into trips, take the minimum cost".
# It's basicly top-down recursion DP without memorization (so full-search).

import sys

sys.setrecursionlimit(100_000)

N, C = map(int, input().split())
S = [0] * (N + 1)  # 1-indexed
F = [0] * (N + 1)  # 1-indexed
for i in range(1, N + 1):
    S[i], F[i] = map(int, input().split())


# Try every way to split groups [start..N] into trips. Return min cost.
def solve(start):
    if start > N:
        return 0
    best = float("inf")
    students = 0
    floors = set()
    for end in range(start, N + 1):  # current trip is groups [start..end]
        students += S[end]
        if students > C:
            break
        floors.add(F[end])
        max_floor = max(floors)
        stops = len(floors)
        trip_cost = max_floor + stops + max_floor
        if end == N:
            trip_cost -= max_floor  # Elevator doesn't go down on last trip
        best = min(best, trip_cost + solve(end + 1))
    return best


print(solve(1))