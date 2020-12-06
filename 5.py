BP = (open('data-5.txt', 'r').read().splitlines())

def read_row(str):
    low = 0
    high = 127
    for i in str[0:6]:
        if i == "F":
            high = (low + high) // 2
        if i == "B":
            low = ((low + high) // 2)+ 1
    if str[6] == "B":
        return high
    elif str[6] == "F":
        return low

def read_col(str):
    low = 0
    high = 7
    for i in str[7:-1]:
        if i == "L":
            high = (low + high) // 2
        if i == "R":
            low = ((low + high) // 2)+ 1
    if str[-1] == "R":
        return high
    elif str[-1] == "L":
        return low

index = []
for i in BP:
    index.append(read_row(i) * 8 + read_col(i))
print("Highest seat ID is {}".format(max(index)))

for i in range(1, len(index)):
    if (min(index) + i) not in index and (min(index) + i) < max(index):
        print("Seat {} is free".format(min(index)+i))
