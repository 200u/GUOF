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

    
# 응용
cnh    = ['자장면', '탕수육', '짬뽕', '깐풍기', '팔보채']
mon    = [5600, 6900, 9000]

whynot = input("메뉴의 입력 > ")
fa     = cnh.index(whynot)

print("선택한 메뉴는", whynot, "비용은", mon[fa], "입니다")
