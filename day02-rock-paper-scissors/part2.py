#!python3

with open('input.txt') as file:
    lines = file.readlines()

score = 0

for line in lines:
    opp, result = [ ord(c) for c in line.split() ]
    opp = opp - ord('A')
    result = result - ord('X')
    score += result * 3
    score += (opp + result - 1) % 3 + 1

print(f'Score: {score}')
