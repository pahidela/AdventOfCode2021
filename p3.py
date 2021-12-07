with open("input3ex.txt", "r") as f:
    data = f.readlines()

bits = len(data[0])-1
info = [0]*bits

for number in data:
    for i in range(bits):
        if number[i] == "1":
            info[i] += 1
        else:
            info[i] -= 1


gamma = ["1" if value > 0 else "0" for value in info]
epsilon = ["1" if value < 0 else "0" for value in info]
gamma_rate = int("".join(gamma),2)
epsilon_rate = int("".join(epsilon),2)
print(f"{gamma_rate}*{epsilon_rate}={gamma_rate*epsilon_rate}")

# Part 2
print(data)
print()
for i in range(bits):
    value = 0
    for number in data:
        value = value+1 if number[i] == "1" else value-1

    winner = "1" if value >= 0 else "0"
    num = len(data)
    for j in range(num):
        print(j, i, data[j][i])
        # if data[j][i] != winner:
        #     del(data[j])
    break
    
print(data)