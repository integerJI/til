user_input = 'Goorm'
user_check = ''

idStart = 0
idEnd = -1
idCheck = 0

if len(user_input) % 2 == 0:
    for i in range(len(user_input)):
        if idCheck % 2 == 0:
            user_check += user_input[idStart]
            idStart += 1
            idCheck +=1
        else :
            user_check += user_input[idEnd]
            idEnd -= 1
            idCheck +=1
else :
    for i in range(len(user_input)):
        if idCheck % 2 == 0:
            user_check += user_input[idStart]
            idStart += 1
            idCheck +=1
        else :
            user_check += user_input[idEnd]
            idEnd -= 1
            idCheck +=1

print(user_check)

