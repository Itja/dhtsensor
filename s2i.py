

with open('/dev/ttyACM0', 'r') as f:
    for line in f:
        print(line)
