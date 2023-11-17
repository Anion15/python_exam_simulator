import random
import time




시험지정답 = []
시험지무작위입력 = []
채점 = []
입력받기 = 0
시험입력무작위 = 0
시험입력같은번호 = 0
시험입력같은번호의번호 = 0
ok = 0
점수총합 = 0
정답개수 = 0
오답개수 = 0
점수 = 0
최고점수 = 0
최고점수시험번호 = 0
최저점수 = 100
최저점수시험번호 = 0
a = 0
while True:
    입력받기 = input("<시험지 입력 방식>\n\n\n1. 무작위 찍기\n2. 한 번호만 찍기\n\n숫자로 입력 : ")
    
    # 입력값이 숫자 또는 소수인지 확인
    try:
        입력받기 = float(입력받기)
        # 입력값이 정수이면서 1 또는 2인지 확인
        if 입력받기.is_integer() and 1 <= int(입력받기) <= 2:
            break
        else:
            print("1부터 2까지의 정수로 입력하세요.")
            print()
            print()
            print()
            print()
            print()
    except ValueError:
        print("숫자를 입력하세요.")
        print()
        print()
        print()
        print()
        print()

# 입력값을 정수로 변환
입력받기 = int(입력받기)

if 입력받기 == 1:
    시험입력무작위 = 1
    시험입력같은번호 = 0

elif 입력받기 == 2:
    시험입력무작위 = 0
    시험입력같은번호 = 1
    print()
    print()
    print()
        
    while True:
        try:
            입력받기 = float(input("1부터 5까지의 정수를 입력하세요: "))
            # 입력값이 정수이면서 1부터 5까지인지 확인
            if 입력받기.is_integer() and 1 <= int(입력받기) <= 5:
                break
            else:
                print("1부터 5까지의 정수로 다시 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")
                
    시험입력같은번호의번호 = int(입력받기)




print()
print()
print()
print()
print()
print()
while True:
    try:
        b = int(input("얼마나 simulation 할건가요? : "))
        if b <= 0:
            print("양의 정수를 입력하세요.")
        else:
            break
    except ValueError:
        print("올바른 숫자를 입력하세요.")

print()
시험지정답 = []
시험지무작위입력 = []
채점 = []
점수총합 = 0
정답개수 = 0
오답개수 = 0
점수 = 0
최고점수 = 0
최고점수시험번호 = 0
최저점수 = 100
최저점수시험번호 = 0
a = 0



#=============================================================

start_time = time.perf_counter()  # 시작 시간 저장


print()
c = 1
if int(c)%100 == 0:
    print(str(c) + "번째.................... " + str(c))
else:
    if int(c)%10 == 0:
        print(str(c) + "번째.......... " + str(c))
    else:
        print(str(c) + "번째. ")
시험지정답 = []
시험지무작위입력 = []
채점 = []
정답개수 = 0
오답개수 = 0
점수 = 0
    
a = 0
while a <= 25:
    a = a + 1
    시험지정답.append(random.randint(1,5))

a = 0
if int(시험입력무작위) == 1:
    while a <= 25:
        a = a + 1
        시험지무작위입력.append(random.randint(1,5))
else:
    if int(시험입력같은번호) == 1:
        while a <= 25:
            a = a + 1
            시험지무작위입력.append(시험입력같은번호의번호)


a = 0
정답개수 = 0
오답개수 = 0
점수 = 0
채점 = []
while a <= 25:
    a = a + 1
    if int(시험지정답[a - 1]) == int(시험지무작위입력[a - 1]):
        정답개수 = 정답개수 + 1
        점수 = 점수 + 4
    else:
        if int(시험지정답[a - 1]) != int(시험지무작위입력[a - 1]):
            오답개수 = 오답개수 + 1

print("정답개수 : " + str(정답개수))
print("오답개수 : " + str(오답개수))
print("점수 : " + str(점수))

if int(점수) > int(최고점수):
    최고점수 = 점수
    최고점수시험번호 = str(c) + "번째 시험"
if int(점수) < int(최저점수):
    최저점수 = 점수
    최저점수시험번호 = str(c) + "번째 시험"
    
점수총합 = 점수총합 + 점수
print()






end_time = time.perf_counter()  # 종료 시간 저장
elapsed_time = end_time - start_time  # 실행 시간 계산

# 실행 시간 출력 (소수점 10자리까지 표현)




a = 0
while a <= 100:
    a = a + 1
    print()
    
print("약 " + str(round(elapsed_time * b, 2)) + "초가 소요됩니다.")

time.sleep(3)

#=========================start program==============================





print()
c = 0
while c <= int(b - 1):
    c = c + 1
    if int(c)%100 == 0:
        print(str(c) + "번째.................... " + str(c))
    else:

        print(str(c) + "번째. ")
    시험지정답 = []
    시험지무작위입력 = []
    채점 = []
    정답개수 = 0
    오답개수 = 0
    점수 = 0
    
    a = 0
    while a <= 24:
        a = a + 1
        시험지정답.append(random.randint(1,5))


    a = 0
    if int(시험입력무작위) == 1:
        while a <= 25:
            a = a + 1
            시험지무작위입력.append(random.randint(1,5))
    else:
        if int(시험입력같은번호) == 1:
            while a <= 25:
                a = a + 1
                시험지무작위입력.append(시험입력같은번호의번호)


    
    a = 0
    정답개수 = 0
    오답개수 = 0
    점수 = 0
    채점 = []
    while a <= 24:
        a = a + 1
        if int(시험지정답[a - 1]) == int(시험지무작위입력[a - 1]):
            정답개수 = 정답개수 + 1
            점수 = 점수 + 4
        else:
            if int(시험지정답[a - 1]) != int(시험지무작위입력[a - 1]):
                오답개수 = 오답개수 + 1

    print("정답개수 : " + str(정답개수))
    print("오답개수 : " + str(오답개수))
    print("점수 : " + str(점수))

    if int(점수) > int(최고점수):
        최고점수 = 점수
        최고점수시험번호 = str(c) + "번째 시험"
    if int(점수) < int(최저점수):
        최저점수 = 점수
        최저점수시험번호 = str(c) + "번째 시험"
    
    점수총합 = 점수총합 + 점수
    print()

print()
print()
print()
print()
print("평균 : " + str(int(점수총합) / int(b)) + "점")
print()
print()
print("최고점수 : " + str(최고점수) + "점 (" + str(최고점수시험번호) + ")")
print("최저점수 : " + str(최저점수) + "점 (" + str(최저점수시험번호) + ")")
