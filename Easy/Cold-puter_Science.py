import sys

n = int(sys.stdin.readline().strip())
t = sys.stdin.readline().strip().split()

y=0
for x in t:
    if int(x) < 0:
        y+=1
print(y)
