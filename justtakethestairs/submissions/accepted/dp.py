
N, C = map(int, input().split())
S = [0] * (N+1) #1-indexed
F = [0] * (N+1) #1-indexed
for i in range(1, N+1):
    S[i], F[i] = map(int, input().split())

solution = [float("inf")]*(N+1)
solution[0] = 0 #Base case
for i in range(1, N+1):
    students = 0
    floors = set()
    for j in range(i - 1, -1, -1):
        students += S[j+1]
        if students > C:
            break
        floors.add(F[j+1])
        max_floor = max(floors)
        stops = len(floors)
        trip_cost = max_floor + stops + max_floor
        if i == N:
            trip_cost -= max_floor #Elevator doesn't go down on last trip
        if solution[j] + trip_cost < solution[i]:
            solution[i] = solution[j] + trip_cost
print(solution[N])
