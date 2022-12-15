#!python3

def add_range(range_list, new_range):
    n_lo, n_hi = new_range
    for existing_range in range_list:
        e_lo, e_hi = existing_range
        if not ( ( n_lo < e_lo - 1 and n_hi < e_lo - 1 ) or ( n_lo > e_hi + 1 and n_hi > e_hi + 1 ) ):
            range_list.remove(existing_range)
            combined_range = (min(n_lo, e_lo), max(n_hi, e_hi))
            range_list.append(combined_range)
            return True
    range_list.append(new_range)
    return False

def unify_ranges(range_list):
    modified = True
    while modified:
        modified = False
        buf = range_list.copy()
        range_list.clear()
        for r in buf:
            if add_range(range_list, r):
                modified = True


with open('input.txt') as file:
    input_lines = file.read().splitlines()

aux_l1 = len('Sensor at ')
aux_l2 = len('closest beacon is at ')

coord_max = 4000000

cave_map = [ [] for _ in range(coord_max + 1) ]

line_count = len(input_lines)
for i in range(line_count):
    progress = int(100 * (i + 1) / line_count)
    print(f'Processing... {progress}%')
    line = input_lines[i]
    sensor_def, beacon_def = line.split(': ')
    s_x, s_y = [ int(n[2:]) for n in sensor_def[aux_l1:].split(', ') ]
    b_x, b_y = [ int(n[2:]) for n in beacon_def[aux_l2:].split(', ') ]
    d_x = abs(b_x - s_x)
    d_y = abs(b_y - s_y)
    sensor_range = d_x + d_y
    start_y = max(0, s_y - sensor_range)
    end_y = min(coord_max, s_y +  sensor_range)
    for y in range(start_y, end_y):
        inv_delta = sensor_range - abs(s_y - y)
        start_x = max(0, s_x - inv_delta)
        end_x = min(coord_max, s_x + inv_delta)
        add_range(cave_map[y], (start_x, end_x))

for range_list in cave_map:
    unify_ranges(range_list)

for y in range(coord_max + 1):
    line = cave_map[y]
    if not line[0] == (0, coord_max):
        taken = set()
        for r in line:
            r_start, r_end = r
            taken |= set(range(r_start, r_end + 1))
        x = (set(range(coord_max + 1)) - taken).pop()
        break

tuning_frequency = 4000000 * x + y
print(f'Tuning frequency: {tuning_frequency}')
