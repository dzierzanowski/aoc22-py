#!python3

with open('input.txt') as file:
    moves = file.read().splitlines()

length = 10
pos = [ [0, 0] for _ in range(length) ]
visited = [
    { tuple(p) } for p in pos
]

for move in moves:
    direction, steps = move.split()
    steps = int(steps)

    idx =  0 if direction in ('L', 'R') else 1
    sgn = -1 if direction in ('L', 'U') else 1

    for _ in range(steps):
        head = pos[0]
        head[idx] += sgn * 1
        for n in range(1, length):
            head = pos[n - 1]
            tail = pos[n]
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                new_tail = head[:]
                if abs(head[0] - tail[0]) > 1:
                    sub_idx = 0
                    sub_sgn = (head[sub_idx] - tail[sub_idx]) / abs(head[sub_idx] - tail[sub_idx])
                    new_tail[sub_idx] += -sub_sgn * 1
                if abs(head[1] - tail[1]) > 1:
                    sub_idx = 1
                    sub_sgn = (head[sub_idx] - tail[sub_idx]) / abs(head[sub_idx] - tail[sub_idx])
                    new_tail[sub_idx] += -sub_sgn * 1
                tail[:] = new_tail[:]
                visited[n].add(tuple(tail))

result1 = len(visited[1])
result2 = len(visited[9])
print(f'Result 1: {result1}')
print(f'Result 2: {result2}')
