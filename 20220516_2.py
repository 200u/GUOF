# if-else 구문 연습
i = int(input("Type a number which overcomes 50 > "))
if i >= 50:
    print ("[ALERT] The number you'd typed", i, ">= 50.")
else:
    print ("[ALERT] The number you'd typed", i, "< 50.")


# Confirm if input is Even or Odd number
i0 = int(input("Type a number > "))
i1 = i0 % 2 #i0을 2로 나눈 나머지를 i1에 저장
if i1 == 0: #나머지가 0일 경우
    print ("해당 정수", i0, "은(는) 짝수입니다.")
else: #나머지가 1일 경우
    print ("해당 정수", i0, "은(는) 홀수입니다.")


# elif
import datetime

ima = datetime.datetime.now()
gatsu = ima.month

if 3 <= gatsu <= 5:
    print ("Spring.")
elif 6 <= gatsu <= 8:
    print ("Summer.")
elif 9 <= gatsu <= 11:
    print ("Autumn.")
else:
    print ("Winter.")


# Confirm if integer > 0 or same as 0, or < 0
o = int(input("Type any number you want. > "))
if o > 0:
    print ("The number you'd typed", o, "> 0.")
elif o == 0:
    print ("The number you'd typed", o, "= 0.")
else:
    print ("The number you'd typed", o, "< 0.")


# Confirm if exam score is A or B or C or D or F.
sc = int(input("Type your exam score. > "))
if sc >= 90:
    print ("Your grade is A.  ", "Score :", sc)
elif sc >= 80:
    print ("Your grade is B.  ", "Score :", sc)
elif sc >= 70:
    print ("Your grade is C.  ", "Score :", sc)
elif sc >= 60:
    print ("Your grade is D.  ", "Score :", sc)
elif sc >= 50:
    print ("Your grade is F.  ", "Score :", sc)
else:
    print ("Lmfao.")

    
# Output Four Patterns (Math Problem)
p_x = int(input("Type X Resolution: > "))
p_y = int(input("Type Y Resolution: > "))

## 1 Patterns
if p_x > 0 and p_y > 0:
    print ("It is 1 Patterns.", "(", p_x, ",", p_y, ")")
## 2 Patterns
elif p_x < 0 and p_y > 0:
    print ("It is 2 Patterns.", "(", p_x, ",",  p_y, ")")
## 3 Patterns
elif p_x < 0 and p_y < 0:
    print ("It is 3 Patterns.", "(", p_x, ",",  p_y, ")")
## 4 Patterns
elif p_x > 0 and p_y < 0:
    print ("It is 4 Patterns.", "(", p_x, ",",  p_y, ")")


# Loop
# for , while.

# while
AO = 1
while AO <= 5: # 조건식이 참인 동안 = AO가 5보다 작은 시간 동안
    print ("문장을 출력한다", AO, "번째 출력")
    AO = AO + 1

# for
for AA in range(5): # range(5) ==> [0, 1, 2, 3, 4] 를 의미     ## List
    print ("문장을 반복!", AA + 1, "번째 출력")
    # IMPORTANT!
    # range starts from 0.


# 리스트 = [0, 1, 2, 3, 4, ...]
    # []에 내부 요소(Element)를 쉼표로 구분하여 입력
    # 출력하면 내부 자료를 모두 출력한다

    # 인덱스(Index) !

    # 0,   1,                   2,                 3,     4
AC = [11, 23, -3.141592653589793238462643383279, "ant", False]
BA = [] #빈 리스트
print (AC[0]) # (AC의 0번 인덱스가 가지고 있는 값) = {11} 을 출력한다
print (AC[1]) # (AC의 1번 인덱스가 가지고 있는 값) = {23} 을 출력한다
print (AC[2]) # (AC의 2번 인덱스가 가지고 있는 값) = {-3.141592653589793238462643383279} 을 출력한다
print (AC[3]) # (AC의 3번 인덱스가 가지고 있는 값) = {"ant"} 을 출력한다
print (AC[4]) # (AC의 4번 인덱스가 가지고 있는 값) = {False} 을 출력한다

# print를 한꺼번에 출력 (응용)
for ii in range(5):
    print (a[ii])

# 번외
print (a[1:3]) # 인덱스 1번부터 2번까지의 값을 출력
    # 결과 : 23, -3.141592653589793238462643383279

print (a[1:]) # 인덱스 1번부터 끝까지의 값을 출력

print (a[:4]) # 인덱스 처음부터 3번까지의 값을 출력

print (a[-1]) # 인덱스 맨 마지막 끝의 값을 출력
                # 중요

print (a[-2]) # 인덱스 맨 마지막 끝에서 2번째의 값을 출력
                # 중요


# 리스트의 요소를 변경
AC[0] = 994 #대입 연산자를 이용하여 AC의 0번 인덱스를 994로 변경
AC[4] = True #대입 연산자를 이용하여 AC의 4번 인덱스를 True의 불리언(Boolean)으로 변경



## Initialize
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print (c)
    # 결과 : [1, 2, 3, 4, 5, 6]
    # (+) 연산을 하면, 두 개의 리스트를 합친다

d = a * 3
print (d)
    # 결과 : [1, 2, 3, 1, 2, 3, 1, 2, 3]
    # (*) 연산을 하면, a의 리스트가 3번 반복되어 하나로 출력된다

# len 함수
#
# 길이를 구하는 함수이다

print (len(d))
    # 결과 : 9

# 다음 시간에 리스트의 여러 함수 적용하는 시간 갖기.
