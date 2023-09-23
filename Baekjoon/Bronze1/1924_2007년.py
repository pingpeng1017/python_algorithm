day = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())

for i in range(x - 1):
    day += month[i]
    
day = (day + y) % 7

print(week[day])

# import calendar

# x, y = map(int, input().split())

# # 0은 월요일, 1은 화요일, ..., 6은 일요일을 나타냄
# day_of_week = calendar.weekday(2007, x, y)

# # 요일 숫자를 요일 문자열로 변환하여 출력
# days_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# print(days_of_week[day_of_week])