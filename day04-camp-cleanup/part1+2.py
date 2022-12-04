#!python3

with open('input.txt') as file:
    lines = file.read().splitlines()

full_overlaps = 0
any_overlaps = 0

for line in lines:
    lo1, hi1, lo2, hi2 = [
        int(s) for elf in line.split(',') for s in elf.split('-')
    ]
    if (lo1 >= lo2 and hi1 <= hi2) or (lo1 <= lo2 and hi1 >= hi2):
        full_overlaps += 1
    if (lo1 <= lo2 and hi1 >= lo2) or (lo2 <= lo1 and hi2 >= lo1):
        any_overlaps += 1

print(f'Full overlaps: {full_overlaps}')
print(f'Any overlaps: {any_overlaps}')
