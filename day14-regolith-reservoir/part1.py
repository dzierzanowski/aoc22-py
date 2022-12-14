#!python3

with open('input.txt') as file:
    input_str = file.read()

lines_definition =  [
    [
        tuple([
            int(n) for n in pair.split(',')
        ])
        for pair in line.split(' -> ')
    ]
    for line in input_str.splitlines()
]

rock_map = {}

for definition in lines_definition:
    for i in range(len(definition) - 1):
        start_x, start_y = definition[i]
        end_x, end_y = definition[i + 1]
        if start_x == end_x:
            lo = min(start_y, end_y)
            hi = max(start_y, end_y)
            for y in range(lo, hi + 1):
                rock_map[(start_x, y)] = 'r'
        else:
            lo = min(start_x, end_x)
            hi = max(start_x, end_x)
            for x in range(lo, hi + 1):
                rock_map[(x, start_y)] = 'r'

while True:
    sand = (500, 0)
    abyss = False

    while True:
        x, y = sand

        if not [ True for coords in rock_map if coords[0] == x and coords[1] > y ]:
            abyss = True
            break

        y += 1
        if not (x, y) in rock_map:
            sand = (x, y)
            continue

        x -= 1
        if not (x, y) in rock_map:
            sand = (x, y)
            continue

        x += 2
        if not (x, y) in rock_map:
            sand = (x, y)
            continue

        break

    if abyss:
        break
    rock_map[sand] = 's'

sand_count = len([ True for tile in rock_map.values() if tile == 's' ])
print(f'Amount of sand: {sand_count}')
