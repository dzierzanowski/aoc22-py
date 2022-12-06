#!python3

with open('input.txt') as file:
    input_str = file.read()

init, commands = [ block.splitlines() for block in input_str.split('\n\n') ]
init.reverse()

stack_count = int(init.pop(0)[-1])

mem1 = [ [] for _ in range(stack_count) ]
mem2 = [ [] for _ in range(stack_count) ]

for row in init:
    for stack_no in range(9):
        # 1, stack_count * 4, 4
        idx = 1 + stack_no * 4
        if idx >= len(row):
            continue
        box = row[idx]
        if not box == ' ':
            mem1[stack_no].append(box)
            mem2[stack_no].append(box)

for command in commands:
    command_tokenized = command.split()
    count, src, dst = (
        int(command_tokenized[1]),
        int(command_tokenized[3]) - 1,
        int(command_tokenized[5]) - 1
    )
    mem1[dst] += list(reversed(mem1[src][-count:]))
    mem2[dst] += mem2[src][-count:]
    del mem1[src][-count:]
    del mem2[src][-count:]

result1, result2  = '', ''
for column in mem1:
    result1 += column[-1]
for column in mem2:
    result2 += column[-1]

print(f'Result, Crate Mover 9000: {result1}')
print(f'Result, Crate Mover 9001: {result2}')
