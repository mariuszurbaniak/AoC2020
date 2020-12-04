report = []
for line in open('data-1.txt'):
    report.append(line)

report = list(map(int, report))

j = 0
result = 0
for t in range(len(report)):
    x = report[j]
    for i in range(j+1, len(report)):
        y = report[i]
        for k in range(j+2, len(report)):
            z = report[k]
            if (x+y+z) == 2020:
                result = x*y*z
    j += 1

print(result)        