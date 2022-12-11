#!python3

with open('input.txt') as file:
    instructions = file.read().splitlines()

def print_pixel(pos, x):
    if abs(pos - (x + 1)) < 2:
        print('#', end='')
    else:
        print('.', end='')
    if pos == 40:
        print()

x = 1
record = [ x ]
pos = 0

for inst in instructions:
    pos = pos % 40 + 1
    print_pixel(pos=pos, x=x)
    record.append(x)

    if not inst == 'noop':
        pos = pos % 40 + 1
        print_pixel(pos=pos, x=x)
        delta = int(inst.split()[1])
        x += delta
        record.append(x)


result = 0
i = 20
while i < len(record):
    result += i * record[i - 1]
    i += 40

print(f'Result: {result}')
