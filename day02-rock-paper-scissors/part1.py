#!python3

with open('input.txt') as file:
    lines = file.readlines()

score = 0

for line in lines:
    opp, player = [ ord(c) for c in line.split() ]
    opp = opp - ord('A')
    player = player - ord('X')
    score += player + 1
    score += ((player - opp + 1) % 3) * 3

print(f'Score: {score}')
