result = ['1899-13-31', '19001231', '2001-09-04', '1900-02-29', '2021-5-31', '1950-11-30', '1996-02-29', '1999-11-31', '2000-02-29',]
answer = 0

for i in result:

    yy = i[:4]
    mm = i[5:7]
    dd = i[8:]

    if yy.find('-') == -1 :
        yy = int(i[:4])
    else :
        yy = 0


    if mm.find('-') == -1 :
        mm = int(i[5:7])
    else :
        mm = 0
        
    if (dd == '') :
        dd = 0
    elif (dd.find('-') == -1):
        dd = int(i[8:])
    else :
        dd = 0

    if 

    if (1900 <= yy <= 2021) :
        if (1 <= mm <= 12) :                
            if (1 <= dd <= 31) :
                answer += 1
            else :
                continue
        else :
            continue
    else :
        continue

print(answer)
# (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;