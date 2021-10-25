import sys

t = int(sys.stdin.readline().strip())

for testCases in range(t):
    n = int(sys.stdin.readline().strip())
    x = sys.stdin.readline().strip().split()
    minX = 100
    maxX = -1
    for xPos in x:
        if int(xPos) < minX:
            minX = int(xPos)
        if int(xPos) > maxX:
            maxX = int(xPos)
    print((maxX-minX)*2)
