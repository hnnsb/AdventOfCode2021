import os

def main():
    data = getInput('day06')
    new = 8
    reset = 6
    days = 256
    data.sort()
    l = {}
    for i in range(0,9):
        l[i] = data.count(i)

    


    for d in range(days):
        print(d)
        l1 = {}
        for key in l:
            if key == 0:
                if 8 in l1:
                    l1[8] += l[key]
                else:
                    l1[8] = l[key]
                if 6 in l1:
                    l1[6] += l[key]
                else:
                    l1[6] = l[key]
            else:
                if key-1 in l1:
                    l1[key-1] += l[key]
                else:
                    l1[key-1] = l[key]
        l = l1.copy()
    
    sum = 0
    for key in l:
        sum+= l[key]
    print(l)
    print(sum)

    




def getInput(day):
    path = os.path.join(os.getcwd(), f'{day}', f'input {day}.txt')
    file = open(f'{path}','r')
    raw = file.read().split(',')
    inp = [int(x) for x in raw]
    #print(inp)
    
    file.close()

    return inp

if __name__ == '__main__':
    main()