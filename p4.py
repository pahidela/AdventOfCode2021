with open("input4.txt", "r") as f:
    datas = f.readlines()

numbers = datas[0]
data = [line for line in datas if line != "\n"]

boards = [{}]
counter = 0
boardNumber = 0
for i in range(1, len(data)):
    vec = data[i].strip().replace("  ", " ").split(" ")
    for j in range(5):
        boards[boardNumber].update({f"{counter}-{j}": {"value": vec[j], "marked": False}})
    counter += 1
    if counter == 5:
        counter = 0
        boardNumber += 1
        boards.append({})
boards.pop(-1)

def markBoardNumber(board: dict, number: str):
    for key in board.keys():
        if board[key]["value"] == number:
            board[key]["marked"] = True
            return

def checkLinesBoard(board: dict):
    # Check all lines
    for i in range(5):
        for j in range(5):
            if not board[f"{i}-{j}"]["marked"]:
                break
        else:
            return True

    for i in range(5):
        for j in range(5):
            if not board[f"{j}-{i}"]["marked"]:
                break
        else:
            return True
    return False

def calculateFinalScore(board: dict, number: str):
    value = 0
    for i in range(5):
        for j in range(5):
            if not board[f"{i}-{j}"]["marked"]:
                value += int(board[f"{i}-{j}"]["value"])
    return int(number)*value
    
def firstBingo(boards, numbers):
    winners = []
    for number in numbers.split(","):
        for i in range(len(boards)):
            markBoardNumber(boards[i], number)
            # prettyPrintBoard(boards[i])
            if checkLinesBoard(boards[i]):
                finalNumber = number
                winnerBoard = i
                return calculateFinalScore(boards[i], finalNumber)

def lastBingo(boards, numbers):
    winners = []
    for number in numbers.split(","):
        for i in range(len(boards)):
            markBoardNumber(boards[i], number)
            # prettyPrintBoard(boards[i])
            if checkLinesBoard(boards[i]):
                finalNumber = number
                winnerBoard = i
                if winnerBoard not in winners:
                    winners.append(winnerBoard)
                if len(winners) == len(boards):
                    return calculateFinalScore(boards[winners[-1]], finalNumber)

print(f"Part one: Final score is {firstBingo(boards, numbers)}\n")
print(f"Part two: Final score is {lastBingo(boards, numbers)}\n")

    

