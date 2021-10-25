import sys

n = sys.stdin.readline().strip()

stack = []
for i in range(int(n)):
    stack.append(int(sys.stdin.readline().strip()))

while len(stack) != 0:
    print(stack.pop())

