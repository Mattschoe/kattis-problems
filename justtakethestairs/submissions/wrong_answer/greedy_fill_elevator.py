#The basic idea of the greedy wrong solution is:
#"Let's just fill the elevator"

N, C = map(int, input().split())
groups = [tuple(map(int, input().split())) for _ in range(N)]

trips = []
i = 0
while i < N:
    capacity = 0
    floors = set()
    while i < N and capacity + groups[i][0] <= C:
        capacity += groups[i][0]
        floors.add(groups[i][1])
        i += 1
    trips.append(floors)

total_cost = 0
for trip, floors in enumerate(trips):
    max_floor = max(floors)
    stops = len(floors)
    is_last = (trip == len(trips) - 1)
    total_cost += max_floor + stops + (0 if is_last else max_floor)

print(total_cost)



