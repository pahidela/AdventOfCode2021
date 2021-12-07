with open("input2.txt", "r") as f:
    data = f.readlines()

depth = 0
pos = 0
aim = 0
for line in data:
    info = line.replace("\n", "").split(" ")
    command, amount = info[0], int(info[1])
    if command == "forward":
        pos += amount
        depth += amount*aim
    elif command == "up":
        aim -= amount
    else:
        aim += amount

print(depth, pos, depth*pos)
