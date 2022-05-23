#IDLE SHELL을 청소
for i in range(100):
    print (" ")



a = [12, 3.14, 'AAA', False] #리스트
print (type(a)) #자료형이 리스트이다
# 결과 : <class 'list'>

print (a[0]) # 12
print (a[1]) # 3.14
print (a[2]) # 'AAA'
print (a[3]) # False
# 접근은 인덱스 번호로 할 수 있다

a[0] = 100 # 리스트 0번 인덱스의 현재 값을 100으로 변경
# 여기서  " = "  은 대입 연산자이다

print(a) # 결과 값 : [100, 3.14, 'Hi', False]



#
# 복습
#
print(a[1:3]) # 1번 인덱스에서 3번 인덱스까지 값을 가져온다

print (a[1:]) # 1번 인덱스에서 끝 인덱스까지 값을 가져온다

print (a[:3]) # 0번 인덱스에서 2번 인덱스 ([:3-1]) 까지 값을 가져온다

print (a[:]) # 모두 가져온다

print (a[-1]) # 맨 마지막 인덱스의 값을 가져온다

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print (c) # [1, 2, 3, 4, 5, 6]

d = a * 3
print (d) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print (len(d)) # 9 - 길이가 9이다

aa = [1, 2, 3]

aa.append(10) # 10을 추가
#append = 추가의 의미이다. (숙지)

print(aa) # [1, 2, 3, 10]
aa.append(20) # [1, 2, 3, 10, 20]
print(aa)


#
#
#   append = 리스트의 뒤에 요소를 추가한다
#
#   insert = 리스트의 중간에 요소를 추가한다
#
#

aa.insert(0, 100) # a[0] = 100 과 다르다!
# aa 의 0번 인덱스에 100을 추가한다
#   [100, 1, 2, 3, 10, 20]
print (aa)

aa.extend([200, 300, 400, 500])
#   [100, 1, 2, 3, 10, 20, 200, 300, 400, 500]
print(aa)

# 값을 하나만 넣는 append와는 달리 extend는 여러 개의 값을 넣을 수 있다
#
#
#   extend = 값을 여러 개 넣기
#
#

a = [1, 2, 3]
del a[0] # a의 0번 인덱스에 해당하는 값(0)을 지운다
#
# del = delete의 의미
print (a)

#
#   pop() 함수 : 매개 변수가 없을 경우 자동으로 1로 취급한다 --> 마지막 요소를 제거
#
a.pop() # 맨 마지막 인덱스를 지우기(pop)
print (a)
# [2]
#

a.pop(0) # 맨 마지막 인덱스를 또 지우기(pop)
print (a)
# []
#

# 응용 A
list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6] # list_b의 리스트 중, 3번 인덱스에서 (6-1)번 인덱스까지의 값을 지운다

print ("del list_b[3:6]", list_b) # 결과 표시 [0, 1, 2, 6]


# 응용 A
list__ = [0, 1, 2, 3, 4, 5, 6]
list_ = [0, 1, 2, 3, 4, 5, 6]
del list__[:3]
del list_[3:]

print ("del list__[:3]", list__) # [3, 4, 5, 6] - [:3] :: (3-1)번 인덱스까지 값 제거
print ("del list_[3:]", list_) # [0, 1, 2] - [:3] :: 3번 인덱스부터 값 제거


#
# 값을 지정하여 제거하는 메소드 ( remove() 함수를 사용 )
list_why = [1, 2, 1, 2]
list_why.remove(2) # 리스트 중, 2 의 값을 가지는 인덱스만 골라 제거

print ("list_why.remove(2)", list_why)


#
# 모두 제거하는 메소드 ( clear() 함수를 사용 )
list_asd = [0, 1, 2, 3, 4, 5, 6]
list_asd.clear()

print ("clear()", list_asd) # 리스트의 값을 모두 제거
# 결과 값 : []
#


# 응용 A
iiisd = [1, 2, 3, 4, 5]
for i in iiisd :
    print ("REPEATING...", i) # 리스트의 값이 던져진 후 출력되는 것이 반복됨

iasdiqw = [10, 20, 30, 40, 50]
print (10 in iasdiqw) # "iasdiqw 의 리스트에 10이 있는가?" 의 질문이다
# 결과 값 : True (있음)
#
print (10012.123154 in iasdiqw) # "iasdiqw 의 리스트에 10012.123154이 있는가?" 의 질문
# 결과 값 : False (없음)
#


for i in range(5) : # [0, 1, 2, 3, 4]
    print ("PR中...", i)
# 결과 값 : PR중... {0~4}

for i in range(1, 6) : # [1, 2, 3, 4, 5] - 1에서부터 (6-1)까지
    print ("PR中...", i)
# 결과 값 : PR중... {1~5}

for i in range(1, 6, 2): # (n, y, a) :: a가 생략되면 1로 간주된다 (a=몇씩 더할 것인지)
    print ("aaa", i)
    
beau = "beau"
for i in beau: # beau의 자리는 [b, e, a, u]가 된다!
    print (i)
