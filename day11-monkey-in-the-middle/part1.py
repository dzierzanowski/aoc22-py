#!python3

with open('input.txt') as file:
    input_list = file.read().split('\n\n')

monkey_count = len(input_list)

register = {}

for monkey_str in input_list:
    monkey_lines = monkey_str.splitlines()[1:]

    line = monkey_lines.pop(0)
    item_list_str = line.strip().split(maxsplit=2)[-1]
    item_list = [ int(item) for item in item_list_str.split(', ') ]

    line = monkey_lines.pop(0)
    operation = line.strip().split(maxsplit=3)[-1]

    divisor, decision_true, decision_false = [
        int(line.strip().split()[-1])
        for line in monkey_lines
    ]

    idx = len(register)
    register[idx] = {
        'decision_true': decision_true,
        'decision_false': decision_false,
        'divisor':  divisor,
        'inspections': 0,
        'item_list': item_list,
        'operation': operation
    }

for _ in range(20):
    for monkey in register.values():
        while monkey['item_list']:
            monkey['inspections'] += 1
            old = monkey['item_list'].pop(0)
            new = int(eval(monkey['operation']) / 3)
            next_monkey_idx = monkey['decision_true'] if not new % monkey['divisor'] else monkey['decision_false']
            register[next_monkey_idx]['item_list'].append(new)

most_active2, most_active1 = [ monkey['inspections'] for monkey in sorted(register.values(), key=lambda monkey: monkey['inspections'])[-2:] ]
monkey_business = most_active1 * most_active2

print(f'Monkey business: {monkey_business}')
