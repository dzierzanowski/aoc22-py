#!python3

with open('input.txt') as file:
    lines = file.read().split()

result = 0

while lines:
    common = (
        set(lines[0]) & set(lines[1]) & set(lines[2])
    ).pop()
    if common <= 'Z':
        result += 26
        common = common.swapcase()
    result += ord(common) - ord('a') + 1
    del lines[:3]

print(f'Result: {result}')
