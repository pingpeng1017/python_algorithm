n, kim, lim = map(int, input().split())
round = 0

while kim != lim:
    # 각각의 참가자 번호를 다음 라운드로 갱신
    kim -= kim // 2
    lim -= lim // 2
    round += 1

print(round)