while True:
    string = input()
    
    if string == '.':
        break
    
    stack = []
    
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            # 스택이 비어있지 않고, 괄호가 짝이 맞을 경우 pop
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                # 스택이 비어있거나 괄호가 짝이 맞지 않으면 break
                stack.append(i)
                break
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    
    if stack:
        print('no')
    else:
        print('yes')