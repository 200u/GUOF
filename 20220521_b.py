# IDLE 쉘의 청소
for i in range(100):
    print (" ")

    
i = int(input("정수의 점수 입력 > "))
if i >= 60:
    print ("합격입니다")
else:
    print ("불합격입니다")
print ("수고하셨습니다")


# 응용
u = int(input("합격 커트라인의 점수를 입력 > "))
i = int(input("정수의 점수 입력 > "))


# 응용 2
if i < 0 or i > 100:
    print ("범위 초과, 계산 종료")
else:
    if i >= u:
        print ("합격입니다")
    else:
        print ("불합격입니다")
    print ("수고하셨습니다")


# 응용 3
age = int(input("나이 입력 > "))
sh = float(input("키 입력 > "))
if age >= 10 and sh >= 110:
    print ("놀이기구의 탑승 가능")
else:
    print ("두 개 중 한 개 이상의 조건에 부합하지 않음, 종료")


# 자작 1
α = int(input("α 근 입력"))
β = int(input("β 근 입력"))
ai = α+β
print ("이차방정식의 근의 합:", ai)


# 응용 4
s_a = int(input("a의 길이를 입력 > "))
s_b = int(input("b의 길이를 입력 > "))
s_c = int(input("c의 길이를 입력 > "))

ca = s_a**2
cb = s_b**2
cc = s_c**2

if cc < ca + cb:
    print ("예각")
elif cc > ca + cb:
    print ("둔각")
elif cc == ca + cb:
    print (" a^2 + b^2 = c^2, 따라서 c가 빗변인 직각삼각형")
else:
    print ("미판정")
