answer = []

user_input_num = input().split(' ')
user_input_str = input()
n = int(user_input_num[-1])
i_check = 0

# 소문자 a = 97
# 소문자 z = 122
for i in range(len(user_input_str)):
    # for 체크
    i_check += 1

    # 아스키 코드로 변환
    asi_s = ord(user_input_str[i]) + n**i_check

    while True :
        if asi_s > 122 :
            asi_s = int(asi_s - 123) + 97
        
        if asi_s > 96 and asi_s < 123 :
            break
    answer.append(chr(asi_s))

answer = ''.join(answer)

print(answer)