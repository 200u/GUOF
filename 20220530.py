# IDLE SHELL을 청소
for IDLESHELLCLEANING in range(100):
    print (" ")


    
for i in range(5):
    asd = print(i) # 세로로 나열
    asd
print(" ")


# 응용
s = 0
ss = 0
for x in range(1, 11):
    if x % 2 == 0: # x가 짝수인 경우
        s += x # x 중에서 짝수인 수를 s에 저장
    if x % 2 == 1: # x가 홀수인 경우
        ss += x # x 중에서 홀수인 수를 ss에 저장
sss = s + ss # 홀수와 짝수의 합을 sss에 저장
print("짝수의 합은", s)
print("홀수의 합은", ss)
print("짝수와 홀수의 합은", sss)


# while문

L = 0
while L < 10: # 0 ~ 9
    print (format(L+1), "번째 반복 중..") # L+1일 시 1 ~ 10, L일 시 0 ~ 9s
    L += 1

# 임시
for i in range(100):
    print (" ")



# 응용
GG = int(input("단을 입력하세요... > "))

print (" ")
print (GG, "의 구구단을 출력합니다.")
print (" ")

G = 1
while G < 10: # GG * 9 까지
    print (" ")
    print (GG, "*", G, " = ", GG*G)
    G += 1


LI = [1, 2, 1, 2, 2]
LI.remove(2)
print(LI)





aa = [1, 2, 4, 8, 16, 32, 64]
val = 2

while val in aa:
    aa.remove(val)
    print(aa)


aaa = [1, 2, 4, 8, 16, 32, 64, 128]
setval = int(input("리스트에서 지울 값을 입력 > "))

while setval in aaa:
    aaa.remove(setval)
print (aaa)


for i in range(100):
    print (" ")



# 응용
s1 = 0 # 짝수의 합의 값들을 저장할 함수 s1
s2 = 0 # 홀수의 합의 값들을 저장할 함수 s2
p = 1 # p는 1부터 시작

print (p, " ~ 100까지의 합의 값을 계산합니다.")
print (" ")

while p <= 100: # p는 100까지 반복
    if p % 2 == 0: # p가 짝수일 경우
        s1 += p # s1에 저장
    if p % 2 == 1: # p가 홀수일 경우
        s2 += p # s2에 저장
    p += 1
    
s3 = s1 + s2 # 짝수의 합의 값들 + 홀수의 합의 값들을 저장할 함수 s3

print("짝수의 합 :", s1)
print("홀수의 합 :", s2)
print("짝수와 홀수의 합 :", s3)



# 응용 - 제곱 계산

inp = int(input("숫자 n을 n제곱하기 위해 쓰일 n을 입력... > "))
shan = 1
k = 1

print (inp, "의", inp, "제곱을 계산합니다.")
print (" ")

while k <= inp:
    shan = inp**k
    k += 1
print (shan)



###
##  break 키워드와 continue 키워드
#
u = 0
YES = ["ㅇㅇ", "dd", "ㅇ", "d", "y", "Y", "네","sp"]
while True:
    print (format(u), "번째 반복 중임.")
    u += 1 # u = u + 1
    question = input("종료 ? : ")
    if question in YES:
        print ("반복 종료.")
        break


##
#

sdj = [5, 15, 6, 20, 8, 25]

for num in sdj:
    if num < 10: # 10보다 작은 숫자는 다음 반복으로 넘어간다 ( = 10 이하의 값은 Skip)
        continue
    print (num)


# 예제
sut = [1, 2, 3, 4, 5]

for su in sut:
    if su == 4:
        break
    if su % 2 == 0:
        continue
    print(su, end=' ')
print("")
print(su)
