su = float(input("수학 점수 입력: "))
en = float(input("영어 점수 입력: "))
sc = float(input("과학 점수 입력: "))

pos = (su+en+sc) / 3

print("")
print("세 과목의 평균은", pos, "점 입니다")



wt = int(input("何時? : "))
h = wt // 100
m = wt % 100
print(h, "시", m, "분")


n_x = int(input("n_x: "))
n_y = int(input("n_y: "))

print((-n_y)**3+2*(n_x**2)*n_y)
