import sys

heapX = []
heapY = []

x = sys.stdin.readline().strip().split()
y = sys.stdin.readline().strip().split()
z = sys.stdin.readline().strip().split()

heapX.append(int(x[0]))
heapX.append(int(y[0]))
heapX.append(int(z[0]))
heapY.append(int(x[1]))
heapY.append(int(y[1]))
heapY.append(int(z[1]))

heapX.sort()
heapY.sort()

if heapX[1] == heapX[2]:
    x = heapX[0]
else:
    x = heapX[2]
    
if heapY[1] == heapY[2]:
    y = heapY[0]
else:
    y = heapY[2]

print(str(x) + " " + str(y))

