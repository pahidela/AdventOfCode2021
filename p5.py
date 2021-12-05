with open("input5.txt", "r") as f:
    data = f.readlines()

maxValue = 0
pointsList = []
for line in data:
    points = line.replace("\n", "").split(" -> ")
    pairPoints = [[int(point.split(",")[0]),int(point.split(",")[1])] for point in points]
    for point in pairPoints:
        if point[0] > maxValue:
            maxValue = point[0]
        if point[1] > maxValue:
            maxValue = point[1]
    pointsList.append(pairPoints)

markedPoints = {}
for pair in pointsList:
    if pair[0][0] == pair[1][0]:
        if pair[0][1] > pair[1][1]:
            high = pair[0][1]
            low = pair[1][1]
        else:
            low = pair[0][1]
            high = pair[1][1]
        for i in range(low, high+1):
            try:
                markedPoints[f"{pair[0][0]}-{i}"] += 1
            except KeyError:
                markedPoints[f"{pair[0][0]}-{i}"] = 1
        
    elif pair[0][1] == pair[1][1]:
        if pair[1][0] > pair[0][0]:
            high = pair[1][0]
            low = pair[0][0]
        else:
            low = pair[1][0]
            high = pair[0][0]
        for i in range(low, high+1):
            try:
                markedPoints[f"{i}-{pair[0][1]}"] += 1
            except KeyError:
                markedPoints[f"{i}-{pair[0][1]}"] = 1

    # Comment for part one
    elif abs(pair[0][0]-pair[1][0]) == abs(pair[1][1]-pair[0][1]):
        first = "up" if pair[0][0] < pair[1][0] else "down"
        second = "up" if pair[0][1] < pair[1][1] else "down"
        i = pair[0][0]; j = pair[0][1]
        for k in range(abs(pair[0][0]-pair[1][0])+1):
            try:
                markedPoints[f"{i}-{j}"] += 1
            except KeyError:
                markedPoints[f"{i}-{j}"] = 1
            i = i+1 if first == "up" else i-1
            j = j+1 if second == "up" else j-1
            
    else:
        continue

counter = 0
for key in markedPoints.keys():
    if markedPoints[key] >= 2:
        counter += 1

print(f"The number of total points where lines overlap is {counter}")