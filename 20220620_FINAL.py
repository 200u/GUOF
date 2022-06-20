# 매개 변수


# SHELL 청소
def CLEARINGALLX():
    for CLEARINGALLSHELLS in range(100):
        print (" ")

CLEARINGALLX()



# 구분하기 위한 간격 간 공백 마련
def TEMPORARYCLEARING(swap):
    for CLEARINGSHELLS in range(swap):
        print (" ")

swap = int(input("간격 간 어느 정도의 공백을 마련하시겠습니까? > "))

TEMPORARYCLEARING(swap)



    
# 튜플
#       특징 : 값 변경의 불가능
#
a   = (10, 20, 30)
b   = 40, 60, 80

print (a[0]) # 10
print (a[1]) # 20
print (a[2]) # 30
print (a[0:2]) # 인덱스 0 ~ (2-1)까지의 값 = 10, 20
TEMPORARYCLEARING(swap)

print (b[0]) # 40
print (b[1]) # 60
print (b[2]) # 80
print (b[1:]) # 인덱스 1 ~ 끝까지의 값
print (b[:2]) # 인덱스 처음 ~ (2-1)까지의 값
TEMPORARYCLEARING(swap)

print (type(a)) # <class 'tuple'>
print (type(b)) # <class 'tuple'>
TEMPORARYCLEARING(swap)

c, d = 100, 99
print (c) # 100
print (d) # 99
TEMPORARYCLEARING(swap)

#       연산자
#
c = a + b
print (c) # 10, 20, 30, 40, 60, 80
TEMPORARYCLEARING(swap)

d = a * 3 # a를 3 번 반복
print (d)
TEMPORARYCLEARING(swap)


# 함수
#       용어 정리
#
#           제 1 : 함수의 필요성
#
#               1 - 프로그램 코드를 작성하는 과정에서 특정 기능을 수행하는 코드 부분을
#               - 여러 곳에서 자주 사용하는 경우가 있다.
#
#               2 - 특정 기능의 코드 부분을 한데 묶어 이름을 붙여 둔 후, 필요한 곳에서 이름만을
#               - 사용하여 불러올 수 있다
#
#
#           함수의 구분
#
#               사용자 정의 함수
#               - 사용자가 직접 만들어 사용하는 함수
#
#               내장함수
#               - Python에서 미리 만들어 제공하는 input(), print() 함수 등
#
#
#       함수 정의
#       - 함수를 정의한다
#       - 정의해야 하는 것 : 1) 함수 헤더, 2) 함수 main
#
#       함수 호출
#       - 함수를 사용하는 것
#
#       매개 변수
#       - 함수를 호출 시 괄호 내부에 넣는 여러 자료
#
#       리턴값
#       - 함수를 호출하여 최종적으로 나오는 결과

# 사전 청소
for SHELLCLEAR in range(15):
    print (" ")
print (" -------------------------------------------------------- ")
print (" ")


# 함수 예제
def f(x):
    print (2*x + 3)

f(3) # 호출
TEMPORARYCLEARING(swap)

# 가설
#
#                   Type 1 : 입력 값 X, 반환 값 X
#           ( 함수 메인에서 print() 함수를 출력하는 경우 )
def type1():    # 헤더
    print (' Type 1 함수의 호출 결과: ', end='')
    print ("1234")  # main 부분

type1()
TEMPORARYCLEARING(swap)

# 함수 예제 2
def p3t():
    for temp in range (3):
        print ("0")

p3t() # 호출
TEMPORARYCLEARING(swap)

# 가설
#
#                   Type 2 : 입력 값 X, 반환 값 O
#           ( 함수 main에서 return 키워드가 나오는 경우 )
def type2():    # 헤더
    return 'RETURNED'  # main 부분


type2() # 호출
        # (!?) 나오지 않는다
        #
        # 반환형일 경우 print()로 묶는다*
print (' Type 2 함수의 호출 결과: ', end='')
print (type2())

        # return 이 함수 main 내에 존재할 경우
        # 호출할 때 print() 함수로 묶어야 한다!
TEMPORARYCLEARING(swap)

# 가설
#
#                   Type 3 : 입력 값 O, 반환 값 X
#           ( 함수 main에서 return 키워드가 나오는 경우 )
def type3(a):   # 헤더
    print (' Type 3 함수의 호출 결과: ', end='')
    print (a**2)  # main 부분

type3(3) # 호출
TEMPORARYCLEARING(swap)

# 가설
#
#                   Type 4 : 입력 값 O, 반환 값 O
#           ( 함수 main에서 return 키워드가 나오는 경우 )
def type4(b):   # 헤더    # 입력 값이 2 개 이상일 경우 (b, c)로 설정
    return b**2 # main 부분
print (' Type 4 함수의 호출 결과: ', end='')
print (type4(4)) # 4**2 = 16

TEMPORARYCLEARING(swap)



# 매개 변수 - 예제
def yeahyeah_pr(lang, a):           # 헤더
    for yeahyeahpr_f in range (a):  # main 부분
        print (lang)                # main 부분

yeahyeah_pr("Adding a piece of innovation.. Please wait", 20)
TEMPORARYCLEARING(swap)


# 매개 변수 - 응용
# 두 개의 정수를 입력받아 합을 출력하기
def calculator_temp(u, i):
    o = u + i
    for kubun in range(1):
        print (" ")
    print ("합은", o)

u = int(input("첫 번째 정수를 입력하시오 > "))
i = int(input("두 번째 정수를 입력하시오 > "))

calculator_temp(u, i)
TEMPORARYCLEARING(swap)

# 매개 변수 - 응용 2
# 입력된 정수 만큼 별을 입력된 정수 만큼 출력하기
def starbright(star):
    for kubun in range(4):
        print (" ")
    for starglittering in range(star):
        print ("*", end='')
    print (" ")
    print ("출력된 별은 총", star, "개 입니다")

star = int(input("출력하기 위한 별의 갯수를 입력하시오 > "))

starbright(star)
TEMPORARYCLEARING(swap)

# 매개 변수 - 응용 3
# 입력된 정수에 해당하는 구구단을 출력하기
def showingmultiplelist(ku):
    for CLEAR in range(4):
        print (" ")
    for KU_RETURN in range(1, 10):
        print(ku, '*', KU_RETURN, '=', ku * KU_RETURN)
    for CLEAR in range(2):
        print (" ")
    print (ku, "단의 리스트를 마련했습니다.")
    
ku = int(input("출력하기 위한 구구단의 숫자(2, 3, 4, ...) 를 입력하시오 > "))

showingmultiplelist(ku)
TEMPORARYCLEARING(swap)


# 매개 변수 - 응용 4
# 입력된 두 정수에 대하여 평균을 구하여 반환한다
def average_(xi, xo):
    xp = xi + xo
    xp_avg = xp / 2
    return xp_avg

xi = int(input("첫 번째 정수 를 입력하시오 > "))
xo = int(input("두 번째 정수를 입력하시오 > "))

print (average_(xi, xo))
TEMPORARYCLEARING(swap)


# 재귀 함수 - 예제
def fac_ex(k):
    if k == 1:
        return 1
    elif k >= 2:
        return k * fac_ex(k-1)

print (fac_ex(8))
#
# k = 8,
# fac_ex(8) = 8 * fac_ex(8-1)
#           = 8 * 7
#           = 8 * 7 * 6
#           = 8 * 7 * 6 * 5
#           = 8 * 7 * 6 * 5 * ... * 1
#           = 8! (Factorial)
#           = 40320
#
TEMPORARYCLEARING(swap)




# 3자리 야구 게임 - 예제 사용
import random
import os

numbers     = []

cnt_total   = 0
cnt_strike  = 0

rand_num    = str(random.randint(0, 9))

for i in range (3):
    while rand_num in numbers:
        rand_num = str(random.randint(0, 9))
    numbers.append(rand_num)

os.system("cis")

print ("=" * 50)
print (" 야구 게임을 시작합니다!! ")
print ("=" * 50)

while (cnt_strike < 3):
    cnt_strike  = 0
    cnt_ball    = 0

    num = str(input("숫자 3자리를 입력하세요. > "))

    if len(num) == 3:
        for i in range (0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j:
                    cnt_strike += 1
                elif num[i] == numbers[j] and i != j:
                    cnt_ball += 1
                    
        if cnt_strike == 0 and cnt_ball == 0:
            print ("아웃!")
        else:
            output = ""
            if cnt_strike > 0:
                output += "{} 스트라이크".format(cnt_strike)
            if cnt_ball > 0:
                output += "{} 볼".format(cnt_ball)
            print (output.strip())
        cnt_total += 1

print ("*" * 50)
print ("{} 회 만에 성공!!".format(cnt_total))
