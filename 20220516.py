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
