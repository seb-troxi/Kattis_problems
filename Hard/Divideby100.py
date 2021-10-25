import sys

n = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()
zerosM = len(m)-1

if (len(m) > len(n)):
    q = "0." + "0"*(zerosM-len(n)) + n
else:
    q = n[:len(n)-zerosM] + "." + n[len(n)-zerosM:]

stopIndex = -1
while(q[stopIndex] == "0"):
    stopIndex -= 1
 
if stopIndex == -1:
    print(q)
elif q[stopIndex] == ".":
    print(q[:stopIndex])
else:
    print(q[:stopIndex+1])
