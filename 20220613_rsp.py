# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#
#       ▶ Function :: RSP_Game
#
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#
#       ▶ Author : ai27p (github)
#
#       ▶ Date : 2022. 06. 13
#
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#
#       ▶ Description
#       ▶
#       ▶ Python으로 작성된 코드로 즐겁게 가위바위보를 해 보세요.
#       ▶ if, elif 등의 반복 구문을 이용하여 코드를 작성하였습니다.
#
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#
#       ▶ ChangeLog
#       ▶
#       ▶ (+) 반복 횟수 설정 기능 추가
#       ▶ (+) 코드 간편화 및 개체 정리
#
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ



# 개체 정리
R_                          = '바위'
S_                          = '가위'
P_                          = '보'
REPEAT_QUESTION             = "얼마나 반복할까요? > "
REPEATING_ANSWER            = "번 만큼 가위바위보를 반복합니다."
REPEAT_QUESTION_EXCLAMATION = "1 이상의 정수를 입력하세요.  현재 입력된 값 : "
INPUT_QUESTION              = "가위, 바위, 보 중 하나를 입력하시오 > "
RSP_WRONG                   = "앗! 다시 시도해보세요!"
same_MSG                    = "비겼습니다!"
win_MSG                     = "이겼습니다!"
lose_MSG                    = "졌습니다.."
closed                      = "가위바위보가 끝났습니다."
CLEARING                    = " "



for CLEAR in range(100):
    print (CLEARING)

    

REPEATS = int(input(REPEAT_QUESTION))

for repeat in range(5):
    print (CLEARING)

if REPEATS > 0:
    print (REPEATS, REPEATING_ANSWER)
else:
    print (REPEAT_QUESTION_EXCLAMATION, REPEATS)
    


# 가위바위보
for cycles_1 in range(REPEATS):
    import random
    rsp = [R_, S_, P_]
    com = random.choice(rsp)
    inp = input(INPUT_QUESTION)
    if com == inp:
        print (same_MSG)
    else:
        if com == S_ and inp == P_:
            print (lose_MSG)
        elif com == P_ and inp == S_:
            print (win_MSG)
        elif com == R_ and inp == P_:
            print (win_MSG)
        elif com == P_ and inp == R_:
            print (lose_MSG)
        elif com == R_ and inp == S_:
            print (lose_MSG)
        elif com == S_ and inp == R_:
            print (lose_MSG)
        elif inp != rsp:
            print (RSP_WRONG)
            
for CLEAR in range(5):
    print (CLEARING)
    
print (closed)

