import sys

moves = sys.stdin.readline().strip()
currentPos = 1

for i in range(len(moves)):
    if moves[i] == "A":
        if currentPos == 1:
            currentPos = 2
        elif currentPos == 2:
            currentPos = 1
    elif moves[i] == "B":
        if currentPos == 2:
            currentPos = 3
        elif currentPos == 3:
            currentPos = 2
    else:
        if currentPos == 3:
            currentPos = 1
        elif currentPos == 1:
            currentPos = 3
print(currentPos)
        
        
