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
    

    return data

data = getInput('day13')
coms = getComs('day13')

matrix = []
for i in range(1500):
    line = []
    for j in range(1500):
        line.append(' ')
    
    matrix.append(line)

for p in data:
    matrix[p[1]][p[0]] = '#'


def foldLeft(mat, com):
    copy = []
    for row in mat:
        copy.append(row[:com])
    for y, row in enumerate(mat):
        for x, c in enumerate(row):
            if x > com and c == '#':
                dx = x - com
                copy[y][x-2*dx] = '#'
    return copy 

def foldUp(mat, com):
    copy = []
    for row in mat[:com]:
        copy.append(row)
    for y, row in enumerate(mat):
        for x, c in enumerate(row):
            if y > com and c == '#':
                dy = y - com
                copy[y-2*dy][x] = '#'
    return copy 


for com in coms:
    if com[0] == 'x':
        matrix = foldLeft(matrix, int(com[1]))
    elif com[0] == 'y':
        matrix = foldUp(matrix, int(com[1]))

for row in matrix:
    print(row[:15])
print()
for row in matrix:
    print(row[15:])

res = 0
for row in matrix:
    for c in row:
        if c == '#':
            res += 1

print(res)