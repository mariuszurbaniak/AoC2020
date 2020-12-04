data = open('data-3.txt', 'r').read().splitlines()




def slope31(data,x,y):
    trees = 0
    j = x
    for i in range(y, len(data), y):
        
        if i > len(data):
            break
        else:
            if j < len(data[i]):
                if data[i][j] == "#":
                    trees += 1
                j += x
                
        
            else:
                data[i] += open('data-3.txt', 'r').read().splitlines()[i] * (j // len(data[0]))
                if data[i][j] == "#":
                    trees += 1
                j += x
                
    return trees


print(slope31(data,1,1)*slope31(data,3,1)*slope31(data,5,1)*slope31(data,7,1)*slope31(data,1,2))
