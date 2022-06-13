# SHELL CLEAR
for CLR in range(100):
    print (" ")





# 딕셔너리
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "에타중아황산나트륨", "치자황색소"],
    "origin" : "Philippines"
    }

print(dictionary)
#
##
#
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])


# 딕셔너리의 값 변경
dictionary["name"] = "8D 망고 건조"
print("name:", dictionary["name"])



# 딕셔너리 새로 만들기
dic = {}
dic[10] = 'h'
dic[20] = 'c'
dic[30] = 'd'
print(dic)

# 딕셔너리 새로 만들기 - 응용
dic_ex = {}
input_1 = input("키 값을 입력하시오 > ")
input_2 = input("키에 저장할 값을 입력하시오 > ")
dic_ex[input_1] = input_2
print(dic_ex)

# 딕셔너리 삭제
del dic[10]
print(dic) # dic 딕셔너리의 10 Key를 삭제하면 'b'도 같이 삭제된다


# 딕셔너리 + for 반복문
for key in dictionary:
    # 출력
    print (key, ":", dictionary[key])


# dic.items()
print(dic.items()) # 튜플 형식으로 출력됨

# dic.keys()
print(dic.keys()) # 키 값만 출력됨

# dic.values()
print(dic.values()) # Value 값만 출력됨


for clear in range(10):
    print (" ")










# 튜플 - 심화

def test():
    return (10, 20)

a, b = test()

print ("a:", a)
print ("b:", b)
