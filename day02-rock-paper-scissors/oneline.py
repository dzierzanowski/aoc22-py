#!python3

print(sorted([
    sum([ int(item) for item in eq.split() ])
    for eq in open('input.txt').read().split("\n\n")
])[-1])
