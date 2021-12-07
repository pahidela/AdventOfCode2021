with open("input1.txt", "r") as f:
    data = f.readlines()

c = 0
for i in range(1, len(data)):
    num = int(data[i].replace("\n", ""))
    if int(data[i].replace("\n", "")) > int(data[i-1].replace("\n", "")):
        c += 1

print(c)
