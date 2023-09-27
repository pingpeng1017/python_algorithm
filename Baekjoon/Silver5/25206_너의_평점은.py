# 등급에 따른 과목평점 정의
grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
    "P": None
}

# 총 학점과 전공과목별의 합 초기화
total_score = 0
total_grade_point = 0

for _ in range(20):
    subject, score, grade = input().split()
    
    # 등급이 P가 아닌 경우
    if grade != "P":
        total_score += float(score)
        total_grade_point += float(score) * grade_to_score[grade]

# 전공평점 계산
result = total_grade_point / total_score

# 소수점 아래 6자리까지 출력
print(format(result, ".6f"))