#!python3

with open('input.txt') as file:
    lines = file.read().split()

result = 0

for line in lines:
    half = int(len(line) / 2)
    common = (
        set( line[:half] ) & set( line[half:] )
    ).pop()
    if common <= 'Z':
        result += 26
        common = common.swapcase()
    result += ord(common) - ord('a') + 1

print(f'Result: {result}')
