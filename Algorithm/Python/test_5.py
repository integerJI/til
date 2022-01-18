grades = ["DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"]	

grades_split = []
grades_index = -1

grades_in = []

def grades_control(a):
    if a == 'A+' :
        return 20
    elif a == 'A0' :
        return 19
    elif a == 'A-' :
        return 18
    elif a == 'B+' :
        return 17
    elif a == 'B0' :
        return 16
    elif a == 'B-' :
        return 15
    elif a == 'C+' :
        return 14
    elif a == 'C0' :
        return 13
    elif a == 'C-' :
        return 12
    elif a == 'D+' :
        return 11
    elif a == 'D0' :
        return 10
    elif a == 'D-' :
        return 9
    else :
        return 1

# print(grades[0].replace(int(grades[0][-2:]), grades_control(int(grades[0][-2:]))))

for i in grades:
    grades_in.append(i.replace(i[-2:],str(grades_control(i[-2:]))))

print(set(grades_in))

