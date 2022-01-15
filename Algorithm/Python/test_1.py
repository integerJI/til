ball = [1, 2, 3, 4, 5, 6]		
order = [6, 2, 5, 1, 4, 3]	
result = [6, 5, 1, 2, 4, 3]

answer = [];
check = 0;

while True:
    if ( ball[0]  == order[check] ) :
        answer.append(order[check])
        a = ball.index(order[check])
        b = order.index(order[check])
        ball.pop(a)
        order.pop(b)
        check = 0
        
    elif ( ball[-1] == order[check] ) :
        answer.append(order[check])
        a = ball.index(order[check])
        b = order.index(order[check])
        ball.pop(a)
        order.pop(b)
        check = 0
    else :
        check += 1
        
    if (len(answer) == len(result)):
        break

print(answer)