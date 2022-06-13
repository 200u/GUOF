a = {1, 2, 1, 2, 3} # {1, 2, 3}
print (a)

b = set([1, 2, 1, 2, 3, 4, 4, 5]) # {1, 2, 3, 4, 5}
print (b)


# intersection()

# union()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

inters = s1.intersection(s2)
print(inters) # 교집합

unions = s1.union(s2)
print(unions) # 합집합

differes = s1.difference(s2)
print(differes) # 차집합

s1.add(4) # 값 1개 추가 :: add
print(s1)

s1.update([4, 5, 999]) # 값 여러 개 추가 :: update
print(s1)

s1.remove(2) # 특정 값 제거 :: remove
print(s1)
