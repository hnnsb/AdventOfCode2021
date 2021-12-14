import os
from copy import deepcopy
from collections import defaultdict

def getInput(day: str):
    path = os.path.join(os.getcwd(),f'{day}', f'input {day}.txt')

    file = open(f'{path}', 'r')
    raw = file.readlines()
    inp = [x.strip('\n').split(',') for x in raw]
    e = [[0 for _ in row] for row in inp]
    for i,row in enumerate(inp):
        for j,x in enumerate(row):
            e[i][j] = int(x)
    
    file.close()

    return e

def getComs(day:str):
    path = os.path.join(os.getcwd(),f'{day}', f'commands.txt')

    file = open(f'{path}', 'r')
    data = []
    for line in file:
        l = line.replace('fold along ', '').strip('\n').split('=')
        data.append(l)
    
    file.close()
    return data

data = getInput('day13')
coms = getComs('day13')


def foldLeft(data, com):
    for p in data:
        if p[0] > com:
                dx = p[0] - com
                p[0] -= 2*dx
    return data 

def foldUp(data, com):
    for p in data:
        if p[1] > com:
                dy = p[1] - com
                p[1] -= 2*dy
    return data 
    


for com in coms:
    if com[0] == 'x':
        data = foldLeft(data, int(com[1]))
    elif com[0] == 'y':
        data = foldUp(data, int(com[1]))

l = []
for y in range(10):
    s = ''
    for x in range(40): 
        if [x,y] in data:
            s += '#'
        else:
            s += ' '
    print(s)

