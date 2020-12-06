lines = list((open('data-6.txt', 'r').read().split("\n\n")))
sum, sum1 = 0, 0
for i in lines:
    if len(i.split()) == 1:
        sum += len(i)
    elif len(i.split()) > 1:
        for j in (i.split()[0]):
            ans = 0
            for k in i.split():
                if j in k:
                    ans += 1
            if ans == len(i.split()):
                sum += 1

       
        
    sum1 += len(set(i.replace('\n','')))
print(sum1)
print(sum)