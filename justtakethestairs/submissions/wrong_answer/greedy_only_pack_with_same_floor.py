#Tries to only pack the elevator with students
#who are going to the same floor. Should fail, not optimal

N, C = map(int, input().split())
groups = [tuple(map(int, input().split())) for _ in range(N)]

trips = []
i = 0
while i < N:
    capacity = groups[i][0]
    floor = groups[i][1]
    i += 1
    #Keep adding only if same floor AND fits
    while i < N and groups[i][1] == floor and capacity + groups[i][0] <= C:
        capacity += groups[i][0]
        i += 1
    trips.append(floor)

total_cost = 0
for trip, floor in enumerate(trips):
    is_last = (trip == len(trips) - 1)
    total_cost += floor + 1 + (0 if is_last else floor)

print(total_cost)