# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def string_veautift(original):
    org_check = ""
    org_check += original[0]
    for i in range(1, len(original)):
        if (original[i-1] == 'a' or original[i-1] == 'e' or original[i-1] == 'i' or original[i-1] == 'o' or original[i-1] == 'u'):
            if original[i] == 'a' or original[i] == 'e' or original[i] == 'i' or original[i] == 'o' or original[i] == 'u':
                pass
            else :
                org_check += original[i]
        else :
            org_check += original[i]

    return org_check

n = int(input())

for i in range(n):
    original = input().strip()
    output = string_veautift(original)
    print(output)
