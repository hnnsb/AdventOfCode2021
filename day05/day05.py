
# x1 = 0, y1 = 1, x2= 2, y2 = 3

def main():
    data = getInput('day05/input day05.txt')
    x1,y1,x2,y2 = 0,1,2,3
    xMax, yMax = getMax(data)
    vents = [[0 for i in range(xMax+1)] for j in range(yMax+1)]

    for coor in data:
        if coor[x1] == coor[x2]:
            if coor[y1] < coor[y2]:
                interval = range(coor[y1],coor[y2]+1)
            else:
                interval = range(coor[y2],coor[y1]+1)

            for y in interval:
                vents[y][coor[x1]] += 1
        elif coor[y1] == coor[y2]:
            if coor[x1] < coor[x2]:
                interval = range(coor[x1],coor[x2]+1)
            else:
                interval = range(coor[x2],coor[x1]+1)

            for x in interval:
                vents[coor[y1]][x] += 1

        #Part Two: Diagonal lines:
        
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
    

def getInput(path):
    file = open(f'{path}','r')
    #inp = file.read().split(',')
    #print(inp)
    
    raw = [x for x in file.read().split('\n') ]
    #raw = file.readlines()
    raw = [x.replace(' -> ', ',')for x in raw]
    inp = [x.split(',') for x in raw]
    inp = [[int(x) for x in sublist] for sublist in inp]
    
    file.close()

    return inp

if __name__ == '__main__':
    main()