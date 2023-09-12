vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    sentence = input()
    if sentence == '#':
        break
        
    cnt = 0
    for i in sentence:
        if i in vowels:
            cnt += 1
            
    print(cnt)