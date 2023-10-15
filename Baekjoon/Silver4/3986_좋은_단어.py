n = int(input())
words = []

for _ in range(n):
    words.append(input())

count = 0
stack = []

for word in words:
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        count += 1
    stack = []

print(count)