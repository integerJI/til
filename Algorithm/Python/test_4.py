import sys

mod = sys.modules[__name__]

input_count = int(input())

for i in range(1,input_count+1):
    globals()['list_{}'.format(i)] = []

while_check = 1

union_check = []

while True :
    input_order = input().split(' ')

    input_client = int(input_order[0])
    input_time = int(input_order[1])
    output_time = int(input_order[2])

    for j in range(input_time,output_time+1):
        union_check.append(j)
        # getattr(mod, 'list_{}'.format(input_client)).append(j)
    
    while_check += 1

    if while_check == input_count+1 :
        break

count={}

for i in union_check:
    try: count[i] += 1
    except: count[i]=1

print(count)
print(union_check)