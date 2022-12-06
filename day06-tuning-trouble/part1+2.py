#!python3

with open('input.txt') as file:
    signal = file.read()

# Start of packet
i = 0
while True:
    sub = signal[i:i+4]
    if len(set(sub)) == 4:
        break
    i += 1
sop = i + 4

# Start of message
i = 0
while True:
    sub = signal[i:i+14]
    if len(set(sub)) == 14:
        break
    i += 1
som = i + 14

print(f'Start of packet: {sop}')
print(f'Start of message: {som}')
