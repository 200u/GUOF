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






# if 문
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
    
