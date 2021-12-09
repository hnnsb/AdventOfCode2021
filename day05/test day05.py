
data = [
[0,9,5,9],
[8,0,0,8],
[9,4,3,4],
[2,2,2,1],
[7,0,7,4],
[6,4,2,0],
[0,9,2,9],
[3,4,1,4],
[0,0,8,8],
[5,5,8,2]
]

def getOverlapping(data):
    res = 0
    for row in data:
        for el in row:
            if el > 1:
                res += 1

    return res

def getMax(li):
    xmax,ymax = 0,0
    for subL in li:
        for index, el in enumerate(subL):
            if(index % 2 == 0):
                if el > xmax:
                    xmax = el
            else:
                if el > ymax:
                    ymax = el
    
    return xmax,ymax

x1,y1,x2,y2 = 0,1,2,3
xMax, yMax = getMax(data)
vents = [[0 for i in range(xMax+1)] for j in range(yMax+1)]

for coor in data:
    a = 0
    b = 0
    if coor[x1] == coor[x2]:
        if coor[y1] < coor[y2]:
            a = coor[y1]
            b = coor[y2]
        else:
            a = coor[y2]
            b = coor[y1]
        for y in range(a,b+1):
            vents[y][coor[x1]] += 1
    elif coor[y1] == coor[y2]:
        if coor[x1] < coor[x2]:
            a = coor[x1]
            b = coor[x2]
        else:
            a = coor[x2]
            b = coor[x1]
        for x in range(a,b+1):
            vents[coor[y1]][x] += 1

    elif abs(coor[x1] - coor[x2]) == abs(coor[y1] - coor[y2]):
            for m in range(abs(coor[x1] - coor[x2])+1):
                if coor[x1] < coor[x2] and coor[y1] < coor[y2]:
                    vents[coor[y1]+m][coor[x1]+m] += 1
                
                elif coor[x1] > coor[x2] and coor[y1] < coor[y2]:
                    vents[coor[y1]+m][coor[x1]-m] += 1
                
                elif coor[x1] < coor[x2] and coor[y1] > coor[y2]:
                    vents[coor[y1]-m][coor[x1]+m] += 1
                
                elif coor[x1] > coor[x2] and coor[y1] > coor[y2]:
                    vents[coor[y1]-m][coor[x1]-m] += 1

overlapping = getOverlapping(vents)
print(overlapping)

