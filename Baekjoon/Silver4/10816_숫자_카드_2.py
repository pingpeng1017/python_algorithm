n = int(input())
card = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
count = {}

for i in card:
    if i in count:  # 딕셔너리에 해당 숫자가 이미 있을 경우
        count[i] += 1
    else:  # 없을 경우 1로 초기화
        count[i] = 1
        
for i in target:
    result = count.get(i)  # 해당 숫자의 개수 가져오기
    if result is None:
        print(0, end=" ")
    else:
        print(result, end=" ")