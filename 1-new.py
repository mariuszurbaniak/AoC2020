import itertools, math

report = list(map(int, (open('data-1.txt', 'r').read().splitlines())))

for i in itertools.combinations(report, 3):
    if sum(i) == 2020:
        result = math.prod(i)

print(result)        