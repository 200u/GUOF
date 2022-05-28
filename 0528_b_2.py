# IDLE SHELL을 청소
for i in range(100):
    print (" ")


a = ['a', 'b', 'c', 'd', 'e', 'f']
a.append('xxas') # 맨 마지막 자리에 추가
print(a)
print(a[1] + a[0] + a[-1])


# 응용
aa = []
aaa = input("입력 > ")
aa.append(aaa)
print (aa)



print (a[1:6:2]) # 1부터 (6-1)까지 2씩 증가 = 1, 3, 5번 인덱스의 값을 정렬
print (a[-4:-1]) # 뒤에서 4번째(-4)부터 (-1-1)번째 인덱스까지의 값을 정렬


# insert = 어느 한 인덱스에 값을 추가
a.insert(2, "ASDFG") # 2번 인덱스에 "ASDFG" 문자열 추가
print (a)


# 입력받은 값으로 인덱스를 삭제
char = input("인덱스의 삭제 > ")
if char in a:
    a.remove(char)
    print (a)
else:
    print (" ")
    print (" ??? ")
    print (" ")

# 리스트 a에 있는 인덱스의 값들을 하나씩 배열시킨다
for i in a:
    print(i)

# 임시로 청소
for i in range(20):
    print (" ")

# 리스트 a에 있는 인덱스의 값들을 하나씩 가로의 형태로 배열시킨다
for i in a:
    print(i, end=' ')
print()
# 둘 다 똑같이 출력된다
for i in range(len(a)): #a의 길이만큼 반복 :: [len()]
    print (a[i], end=' ')

a.sort(reverse = True) # 리스트 a의 인덱스가 reverse되어 정렬된다
print(a)
print()
li = sorted(a) # sorted = 정렬된 상태의 리스트를 생성한다
print(li)


# 응용
cnh    = ['자장면', '탕수육', '짬뽕', '깐풍기', '팔보채']
mon    = [5600, 6900, 9000]

whynot = input("메뉴의 입력 > ")
fa     = cnh.index(whynot)

print("선택한 메뉴는", whynot, "비용은", mon[fa], "입니다")


import random
y = [ ]
y.append("a")
y.append("s")
y.append("d")
y.append("f")
y.append("g")

print(y)

print("오늘의 영단어")
ch = random.randint(0, 4) # 0 ~ 4의 인덱스 범위에서 한 개(個)를 뽑기(選)
print(y[ch])



# !
import turtle
t = turtle.Turtle()
t.speed(0) # 거북이의 속도는 0 으로 설정하면 최대가 됩니다
t.width(3) #거북이가 그리는 선의 두께는 width() 를 호출합니다
length = 10 # 초기 선의 길이는 10 으로 합니다

#색상은 리스트에 저장했다가 하나씩 꺼내서 변경하도록 합니다
colors = ["red", "purple", "blue", "green", "yellow", "orange" ]
# while
#반복문이다 . 선의 길이가 500 보다 작으면 반복 .
while length < 500:
    t.forward (length)# length 만큼 전진합니다 .
    t.pencolor (colors[length%6])# 선의 색상을 변경합니다
    t.right(89)# 89 도 오른쪽으로 회전합니다
    length += 5
# 선의 길이를 5 만큼 증가합니다




t_l = [0, 10, 20, 30]
v_l = [4.8, 9.4, 17.3, 30.4]

vv = float(input("수증기량 입력 > "))
tt = int(input("온도 입력 > "))

if tt in t_l:
    hu = ( vv / v_l[t_l.index(tt)] ) * 100
    print ("습도는", hu, "% 입니다")
print ("프로그램을 종료")
