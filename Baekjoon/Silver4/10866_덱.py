from collections import deque
import sys

n = int(sys.stdin.readline())
d = deque ()

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push_front':
        d.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        d.append(int(command[1]))
    elif command[0] == 'pop_front':
        print(d.popleft() if d else -1)
    elif command[0] == 'pop_back':
        print(d.pop() if d else -1)
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        print(int(not d))  # True를 1로, False를 0으로
    elif command[0] == 'front':
        print(d[0] if d else -1)
    elif command[0] == 'back':
        print(d[-1] if d else -1)