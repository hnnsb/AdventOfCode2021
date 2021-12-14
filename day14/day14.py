import os
from copy import deepcopy
from collections import defaultdict, Counter
from typing import Counter

def getInput(day: str):
    path = os.path.join(os.getcwd(),f'{day}', f'input {day}.txt')
    # path = os.path.join(os.getcwd(),f'{day}', f'input {day}_ex.txt')
    file = open(f'{path}', 'r')
    raw = file.readlines()
    d ={}
    for line in raw:
        a,b = line.strip('\n').split(' -> ')
        d[a] = b
    # inp = [line.strip('\n').split(' -> ') for line in raw]
    return d

x = 'VNVVKSNNFPBBBVSCVBBC'
# x = 'NNCB'

ins = getInput('day14')

print('Part 1:')
# days = 10
# for _ in range (days):
#     # print(_)
#     off = 0
#     new_x = ''
#     for i, c in enumerate(x):
#         new_x += c
#         for key in ins:
#             if x[i:i+2] == key:
#                 new_x += ins[key]
#                 off +=1
#                 break
#     x = new_x

# count = Counter(x)
# mc = count.most_common()
# print(mc[0][1]-mc[-1][1])


print('Part 2:')


x = 'VNVVKSNNFPBBBVSCVBBC'

nc = {}
cc ={}
for i,c in enumerate(x):
    if c not in cc:
        cc[c] = 1
    else:
        cc[c] += 1
    if len(x[i:i+2]) == 2:
        if x[i:i+2] not in nc:
            nc[x[i:i+2]] = 1
        else:
            nc[x[i:i+2]] += 1

# print(nc)

days = 40
for _ in range (days):
    print(_)
    nc_new = nc.copy()
    for key in ins:
        if key in nc:
            if ins[key] not in cc:
                cc[ins[key]] = nc[key]
            else:
                cc[ins[key]] += nc[key]
            
            if key[0]+ins[key] not in nc_new:
                nc_new[key[0]+ins[key]] = nc[key]
            else:
                nc_new[key[0]+ins[key]] += nc[key]

            if ins[key]+key[1] not in nc_new:
                nc_new[ins[key]+key[1]] = nc[key]
            else:
                nc_new[ins[key]+key[1]] += nc[key]

            nc_new[key] -= nc[key]
    nc_new = {k : v for k, v in nc_new.items() if v != 0}
    nc = nc_new

count = Counter(cc)
mc = count.most_common()
print(mc[0][1]-mc[-1][1])