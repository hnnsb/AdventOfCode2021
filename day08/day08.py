

def getInput(path):
    file = open(f'{path}', 'r')
    raw = file.readlines()
    raw = [x.strip('\n') for x in raw]
    inp = [x.split(' | ') for x in raw]
    inp = [[x[0].split(' '),x[1].split(' ')] for x in inp]
    

    file.close()

    return inp


def str_minus(s:str, t:str):
    for c in t:
        if c in s:
            s = s.replace(c,'')

    return s

def matcher(d: str, e):
    # 2, 3, 5
    if len(d) == 5:
        if match(e[1], d):
            e[3] = d
        elif match(str_minus(e[4], e[1]), d):
            e[5] = d
        else:
            e[2] = d

    elif len(d) == 6:
        if match(e[4], d):
            e[9] = d
        elif match(e[1], d):
            e[0] = d
        else:
            e[6] = d

    return e

def match(a, b):
    for c in a:
        if c not in b:
            return False
    
    return True


def lookup(d, ex):
    for key in ex:
        if match(ex[key],d) and len(d) == len(ex[key]):
              
            return key


print('Part 1:')
data = getInput("input day08.txt")
count = 0
for row in data:
    for digit in row[1]:
        if len(digit) in [2,3,4,7]:
            count += 1

print(count)

print('Part 2:')
t_sum = 0
for row in data:
    
    ex = {}
    for digit in row[0]:
        if len(digit) == 2:
            ex[1] = digit
        elif len(digit) == 3:
            ex[7] = digit
        elif len(digit) == 4:
            ex[4] = digit
        elif len(digit) == 7:
            ex[8] = digit

        if len(ex) == 4:
            break
        # explicit cases, 1(2),4(4),7(3),8(7)
    
    for digit in row[0]:
        ex = matcher(digit, ex)

    res = ''
    for digit in row[1]:
        res += f'{lookup(digit, ex)}'
    
    t_sum += int(res)
            
print(t_sum)        

