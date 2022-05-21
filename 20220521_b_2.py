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
age_ze = int(input("나이 제한을 입력 > "))
sh_ze = int(input("키 제한을 입력 > "))
age = int(input("나이 입력 > "))
sh = float(input("키 입력 > "))
if age >= age_ze and sh >= sh_ze:
    print ("놀이기구에 탑승 가능")
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
    print ("c가 빗변인 직각삼각형")
else:
    print ("미판정")

# 응용 5
ii0_w = "ax²+bx+ c=0"
print ("주어진 이차방정식은", ii0_w, "입니다")
ii0_a = int(input("a에 들어갈 값을 입력하시오 > "))
ii0_b = int(input("b에 들어갈 값을 입력하시오 > "))
ii0_c = int(input("c에 들어갈 값을 입력하시오 > "))
ii0_id__ = ii0_b**2 - 4*ii0_a*ii0_c
print ("입력된 값을 조합하여 완성된 이차방정식의 재료 :", "a =", ii0_a, "b =", ii0_b, "c =", ii0_c)
print (" ")
if  ii0_id__ > 0:
    print ("판별식 > 0 이므로, 해당 이차방정식은 서로 다른 두 개의 근을 가집니다.")
elif ii0_id__ == 0:
    print ("판별식 = 0 이므로, 해당 이차방정식은 한 개의 근을 가집니다.")
elif ii0_id__ < 0:
    print ("판별식 < 0 이므로, 해당 이차방정식은 근을 가지지 않습니다.")
else:
    print ("오류")


    
# 반복문

# for문
for iw in range(5):
    print ("Welcome")
    print (" ")

# while문
ie = 1
while ie <= 9:
    print (ie, "번째 문자 출력 중..")
    print (" ")
    ie = ie + 1

# for문 응용
for ip in range(1, 6, 1):
    print (ip, end="yes")

for il in range(1, 10, 2):
    print (str(il), end = "aaaaaaaa")

xxa = 0
for i in range(1, 101):
    xxa = xxa + i # sum += i 의 형태와 동일
    print (xxa)


# 반복문 + 응용 4
for i in range(5):
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
        print ("c가 빗변인 직각삼각형")
    else:
        print ("미판정")


# 조건 제어
pw = ""
while pw != "0":
    pw = input("암호를 입력: ")
print ("로그인 성공")




# 코드 줄이기 (실습)
import turtle
t = turtle.Turtle()
for i in range(5):
    t.circle(100) # 원의 반지름의 기리
    t.left(60) # 60도의 각도만큼 회전
t.circle(100)

# 정n각형 만들기 (실습)
import turtle
t = turtle.Turtle()
t.shape ("turtle")
nani = int(turtle.textinput("通知", "몇 각형을 원하십니까?"))
for i in range (nani):
    t.forward(100)
    t.left(360/nani)

# 약수 구하기 (실습)
qwertyuiop = int(input("자연수를 입력 : "))
# 소스 이해
for m in range (1, qwertyuiop+1):
    if qwertyuiop % m == 0:
        print (m, end = " , ")
