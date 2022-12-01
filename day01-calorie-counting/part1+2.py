#!python3

with open('input.txt') as file:
    input_str = file.read()

ordered = sorted([
    sum([ int(item) for item in eq.split() ])
    for eq in input_str.split("\n\n")
])

solution1 = ordered[-1]
solution2 = sum(ordered[-3:])

print(f'Most calorie-rich eq: {solution1}')
print(f'Top 3 elves: {solution2}')
