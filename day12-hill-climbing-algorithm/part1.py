#!python3

with open('input.txt') as file:
    heightmap = [ list(line) for line in file.read().splitlines() ]

h = len(heightmap)
w = len(heightmap[0])
inf = h * w

start = None
target = None

for y in range(h):
    for x in range(w):
        if heightmap[y][x] == 'S':
            start = (x, y)
        elif heightmap[y][x] == 'E':
            target = (x, y)
    if start and target:
        break

heightmap[start[1]][start[0]] = 'a'
heightmap[target[1]][target[0]] = 'z'

unvisited = dict([ ((x, y), inf) for y in range(h) for x in range(w) ])

current = start
unvisited[current] = 0
found = False
result = None
while True:
    x, y = current
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        neighbor = (nx, ny)
        if nx in (-1, w) or ny in (-1, h) or neighbor not in unvisited:
            continue
        current_val = ord(heightmap[y][x])
        neighbor_val = ord(heightmap[ny][nx])
        delta = neighbor_val - current_val
        if delta > 1:
            continue
        unvisited[neighbor] = min(unvisited[neighbor], unvisited[current] + 1)
        if neighbor == target:
            result = unvisited[neighbor]
            found = True
            break
    if found:
        break
    del unvisited[current]
    current = sorted(unvisited.items(), key=lambda t: t[1])[0][0]

print(f'Result: {result}')
