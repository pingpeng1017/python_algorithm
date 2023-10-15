t = int(input())

for _ in range(t):
    stack = []
    ps = input()
    result = 'YES'
    
    for i in ps:
        if i == '(':
            stack.append('(')
        else:
            if not stack:  # 스택에 괄호가 없을 경우
                result = 'NO'
                break
            stack.pop()
    
    if stack:
        result = 'NO'

    print(result)