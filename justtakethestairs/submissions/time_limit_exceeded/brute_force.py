#The basic idea of the brute force solution is:
#"Try every possible way to split the groups into trips, take the minimum cost".

N, C = map(int, input().split())
S = [0] * (N + 1)
F = [0] * (N + 1)
for i in range(1, N + 1):
    S[i], F[i] = map(int, input().split())

best = float("inf")
stack = [(1, 0)]
while stack:
    start, cost = stack.pop()
    if start > N:
        best = min(best, cost)
        continue
    students = 0
    floors = set()
    for end in range(start, N + 1):
        students += S[end]
        if students > C:
            break
        floors.add(F[end])
        max_floor = max(floors)
        stops = len(floors)
        trip_cost = max_floor + stops + max_floor
        if end == N:
            trip_cost -= max_floor
        stack.append((end + 1, cost + trip_cost))
print(best)
