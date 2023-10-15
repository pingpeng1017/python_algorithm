n = int(input())
stack = []
result = []

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        result.append(stack.pop() if stack else -1)
    elif command[0] == 'size':
        result.append(len(stack))
    elif command[0] == 'empty':
        result.append(0 if stack else 1)
    elif command[0] == 'top':
        result.append(stack[-1] if stack else -1)

for i in result:
    print(i)