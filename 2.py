import re
data = open('data-2.txt', 'r').read().splitlines()

count1, count2 = 0, 0

for i in data:
    i = re.split("[\- :]+",i)
    if i[3].count(i[2]) >= int(i[0]) and i[3].count(i[2]) <= int(i[1]):
        count1 += 1
    if (i[2] == i[3][int(i[0])-1] and i[2] != i[3][int(i[1])-1]) or (i[2] != i[3][int(i[0])-1] and i[2] == i[3][int(i[1])-1]):
        count2 += 1

print(count1)
print(count2)
