n = int(input())
word_set = set()  # 중복 제거

for _ in range(n):
    word_set.add(input())

word_list = list(word_set)  # 리스트로 변환
word_list.sort()  # 사전 순으로 정렬
word_list.sort(key=len)  # 길이 순으로 정렬

for i in word_list:
    print(i)