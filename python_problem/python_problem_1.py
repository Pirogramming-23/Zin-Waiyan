# 마지막에 31 부른 사람 -> Lose
# 한번 부르면 1~3개의 수만 부를 수 있음

# 1단계
num = 0

# 2단계
# n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))

# 3단계
# while True:
#     try:
#         n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
#         if n not in [1,2,3]:
#             print("1,2,3 중 하나를 입력하세요")
#         else:
#             break
#     except ValueError:
#         print("정수를 입력하세요")

# # 4단계
# for i in range(n):
#     num += 1
#     print(f"playerA : {num}")

# # 5단계
# while True:
#     try:
#         n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
#         if n not in [1,2,3]:
#             print("1,2,3 중 하나를 입력하세요")
#         else:
#             break
#     except ValueError:
#         print("정수를 입력하세요")

# for i in range(n):
#     num += 1
#     print(f"playerB : {num}")


# 6단계
# 0 -> playerA, 1-> playerB
turn = 0
while num<31:
    player = 'playerA' if turn==0 else 'playerB'
    while True:
        try:
            n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if n not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요")
            else:
                break
        except ValueError:
            print("정수를 입력하세요")
    
    for i in range(n):
        num += 1
        print(f"{player} : {num}")
        if num>=31: # 내부 for문 중단
            break
    
    if num>=31:
        break # 외부 while문 중단

    # 텀 바뀌기
    turn = 1 - turn