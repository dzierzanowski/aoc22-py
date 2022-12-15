#!python3

with open('input.txt') as file:
    input_lines = file.read().splitlines()

aux_l1 = len('Sensor at ')
aux_l2 = len('closest beacon is at ')

cave_map = {}

checked_y = 2000000
occupied_set = set()
devices_on_checked_y = set()

for line in input_lines:
    sensor_def, beacon_def = line.split(': ')
    s_x, s_y = [ int(n[2:]) for n in sensor_def[aux_l1:].split(', ') ]
    b_x, b_y = [ int(n[2:]) for n in beacon_def[aux_l2:].split(', ') ]
    if s_y == checked_y:
        devices_on_checked_y.add((s_x, s_y))
    if b_y == checked_y:
        devices_on_checked_y.add((b_x, b_y))
    d_x = abs(b_x - s_x)
    d_y = abs(b_y - s_y)
    delta = d_x + d_y
    delta_from_target_y = abs(checked_y - s_y)
    if delta_from_target_y < (delta + 1):
        delta_on_target_y = abs(delta_from_target_y - delta)
        for step_x in range(-delta_on_target_y, delta_on_target_y + 1):
            coords = (s_x + step_x, checked_y)
            occupied_set.add(coords)

result = len(occupied_set) - len(devices_on_checked_y)
print(f'Result: {result}')
