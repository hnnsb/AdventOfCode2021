def getInput(path):
    file = open(f'{path}', 'r')
    raw = file.readlines()


    inp = [list(x.strip('\n')) for x in raw]
    inp2= inp[:]
    for y,row in enumerate(inp):
        for x,el in enumerate(row):
            inp2[y][x] = int(el)
    

    file.close()

    return inp2

def isLowPoint(x,y,data):

    n1, n2, n3, n4 = [x,y-1],[x-1,y],[x,y+1],[x+1,y]
    N = [n1,n2,n3,n4]
    for n in N:
        if n[0] < 0 or n[0] >= len(data[0]) or n[1] < 0 or n[1] >= len(data):
            continue
    
        if data[n[1]][n[0]] > data[y][x]:
            continue
        else:
            return False
    #print(f'{x,y}: {data[y][x]}')
    return True


print('part 1')
data = getInput('day09/input day09.txt')
#data = getInput('day09/short input.txt')

sum = 0
lowPoints = []
for y,row in enumerate(data):
    for x,loc in enumerate(row):
        if isLowPoint(x,y,data):
            sum += loc + 1
            lowPoints.append([x,y])

print(sum)


def isinbasin(x,y,set: set):
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return
    if (x,y) in set:
        return
    if data[y][x] < 9:
        set.add((x,y))
        isinbasin(x-1,y,set)
        isinbasin(x,y-1,set)
        isinbasin(x+1,y,set)
        isinbasin(x,y+1,set)


print('part2')
basins = []
for lp in lowPoints:
    basin = set()
    size = 0
    dx = 0
    dy = 0
    isinbasin(lp[0],lp[1],basin)
    basins.append(len(basin))

basins.sort()
p = basins[-1]*basins[-2]*basins[-3]
print(p)