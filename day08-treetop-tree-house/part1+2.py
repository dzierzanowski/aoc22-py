#!python3

with open('input.txt') as file:
    input_str = file.read()

grid = [
    [
        int(c) for c in line
    ]
    for line in input_str.splitlines()
]

height = len(grid)
width = len(grid[0])

visible = {}
high_score = 0

for y in range(0, height):
    for x in range(0, width):
        key = (x, y)
        val = grid[y][x]
        # Gather trees around the tree tbat are equal to or higher than the tree
        up    = [ line[x] for line in grid[:y]     if line[x] >= val ]
        down  = [ line[x] for line in grid[y + 1:] if line[x] >= val ]
        left  = [ n for n in grid[y][:x]     if n >= val ]
        right = [ n for n in grid[y][x + 1:] if n >= val ]
        if not (up and down and left and right):
            visible[key] = True
        score_up    = 0
        for n in reversed(range(0, y)):
            score_up += 1
            if grid[n][x] >= val:
                break
        score_down  = 0
        for n in range(y + 1, height):
            score_down += 1
            if grid[n][x] >= val:
                break
        score_left  = 0
        for n in reversed(range(0, x)):
            score_left += 1
            if grid[y][n] >= val:
                break
        score_right = 0
        for n in range(x + 1, width):
            score_right += 1
            if grid[y][n] >= val:
                break

        high_score = max(high_score, score_up * score_down * score_left * score_right)

no_visible = len(visible)

print(f'Number of visible trees: {no_visible}')
print(f'Highest-scored tree: {high_score}')
