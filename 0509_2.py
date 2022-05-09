a = input("값을 입력하세요 : ")
print("클래스 종류는", type(a), "입니다")

#input 함수를 이용한 모든 입력의 자료형은 문자열임
# 자료형 변환하기

# 1) 문자열 --> 정수 int()
# 2) 문자열 --> 실수 float()

n1 = int(input("정수를 입력하세요 :"))
n2 = int(input("2번째 정수를 입력하세요 :"))
res = n1 + n2
print ("첫 번째와 두 번째의 정수 합은", res, "입니다")


# 오비탈의 갯수의 경우의 수
# 응용.
orb1 = float(input("s 오비탈의 가짓 수 : "))
orb2 = float(input("p 오비탈의 가짓 수 : "))
orb3 = float(input("d 오비탈의 가짓 수 : "))
orb4 = float(input("f 오비탈의 가짓 수 : "))

print ("오비탈의 총 가짓수는", orb1+orb2+orb3+orb4, "입니다")

a = float(input("첫 숫자 입력 : "))
b = float(input("두 숫자 입력 : "))
#
#

print("합", a+b)
print("차", a-b)
print("곱", a*b)
print("나눔", a/b)




# print 함수 추가 기능 (sep 인자에 대해)
#
# sep 인자는 텍스트와 텍스트 사이에 넣는 기능이다
#
# sep = separate

s = "s 오비탈"
p = "p 오비탈"
d = "d 오비탈"
f = "f 오비탈"
print(s, p ,d ,f, sep = ' , ')


print('a', end = '')
print('b')


#
# Python에서의 불리언은 True와 False 뿐이다

print(30 == 100)
x = 44
y = 55
print(x<y)
print(x>y)
print(x!=y)

# 논리 연산자를 통한 불리언 연산

#       not = 반대로 전환
#       and = 두 개가 모두 참일 떄 True, 그렇지 않을 시에는 False
#       or = 두 개 중에 하나만 참이여도 true, 모두 거짓일 때는 False

print(not False)
print(not True)






# if 문 (여기서부터)
# 들여쓰기를 잘 해야 오류가 나지 않는다
#
#
#
s = 1 #1
p = s + 2 #3
d = s + p + 2 #5
f = s + p + d
orbital = s + p + d + f

if orbital >= 10:
    print("오비탈의 총 가짓수", orbital, "은 10을 넘었습니다")
if orbital < 10:
    print("X")
    

ㅜ = input("정수를 입력하세요 >")
ㅜ = int(ㅜ)
if ㅜ > 0:
    print("양수")
if ㅜ < 0:
    print("음수")
if ㅜ == 0:
    print("0")


s = 1
p = s + 1
if s < p:
    print ("s 오비탈의 값", s, "은", "p 오비탈", p, "보다 값이 작다! (참)")
print("차회의 문장을 실행")



#
#
# 간단한 숙제 ! (초심자 가능)

aax = int(input('수를 입력 >'))
kekka = aax % 2

if kekka == 0:
    print("kekka 는 짝수였다!")
if kekka == 1:
    print("kekka 는 홀수였다!")



# 정수의 끝자리에 따른 짝수와 홀수를 판별
nannba = input("integer nyoryouku >")

# 정수의 마지막 자리의 수를 추출
last_nann = nannba[-1]

#문자열 last_nann 을 숫자(int) 에 변환
last_2 = int(last_nann)

#짝수의 경우
if last_2 == 0 \
   or last_2 == 2 \
   or last_2 == 4 \
   or last_2 == 6 \
   or last_2 == 8:
    print("짝수였다!")

#홀수의 경
if last_2 == 1 \
   or last_2 == 3 \
   or last_2 == 5 \
   or last_2 == 7 \
   or last_2 == 9:
    print("홀수였다!")
    
