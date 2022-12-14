#!python3

with open('input.txt') as file:
    pairs_str = file.read().split('\n\n')

pairs = [
    tuple([ eval(item) for item in pair.splitlines() ])
    for pair in pairs_str
]
singles = [ item for pair in pairs for item in pair ]

def cmp(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        elif left < right:
            return 1
        else:
            return -1
    if type(left) == int:
        left = [ left ]
    if type(right) == int:
        right = [ right ]
    for i in range(len(left)):
        if i == len(right):
            return -1
        verdict = cmp(left=left[i], right=right[i])
        if verdict:
            return verdict
    if len(right) > len(left):
        return 1
    return 0


idx = 0
right_ordered = set()

while pairs:
    idx += 1
    pair = pairs.pop(0)
    left, right = pair
    if cmp(left, right) == 1:
        right_ordered.add(idx)
result1 = sum(right_ordered)
print(f'Result 1: {result1}')

is_sorted = False
div_packet1 = eval('[[2]]')
div_packet2 = eval('[[6]]')
singles += [ div_packet1, div_packet2 ]

# Bubble sort is enough, right?
# while not is_sorted:
#     is_sorted = True
#     for i in range(len(singles) - 1):
#         left = singles[i]
#         right = singles[i + 1]
#         if cmp(left, right) == -1:
#             tmp = left
#             left = right
#             right = tmp
#             is_sorted = False

# It wasn't. Let's try insertion sort.
sorted_packets = [ singles.pop() ]
while singles:
    left = singles.pop()
    for i in range(len(sorted_packets) + 1):
        if i == len(sorted_packets):
            sorted_packets.append(left)
            break
        right = sorted_packets[i]
        if not cmp(left, right) == -1:
            sorted_packets.insert(i, left)
            break

key1 = sorted_packets.index(div_packet1) + 1
key2 = sorted_packets.index(div_packet2) + 1
decoder_key = key1 * key2
print(f'Decoder key: {decoder_key}')
