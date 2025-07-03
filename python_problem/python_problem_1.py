# 마지막에 31 부른 사람 -> Lose
# 한번 부르면 1~3개의 수만 부를 수 있음

# 1단계
num = 0

# 2단계
# n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))

# 3단계
while True:
    try:
        n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        if n not in [1,2,3]:
            print("1,2,3 중 하나를 입력하세요")
        else:
            break
    except ValueError:
        print("정수를 입력하세요")
    