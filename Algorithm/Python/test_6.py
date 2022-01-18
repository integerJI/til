id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

report_list = []
report_count = {}

for i in range(len(report)):
    report_list.append(report[i].split(' ')[1])

for j in report_list:
    try: 
        report_count[j] += 1
    except: 
        report_count[j] = 1

for key, value in report_count.items():
    if value >= k:
        print(key)