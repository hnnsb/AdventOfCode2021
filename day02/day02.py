import numpy as np
import os

input = []

day = 'day02'
path = os.path.join(os.getcwd(), f'{day}', f'input {day}.txt')
with open(path,'r') as file:
    for line in file:
        inner_list = [elt.strip() for elt in line.split()]
        input.append(inner_list)

file.close()

hPos = 0
depth = 0

for dir in input:
    if dir[0] == 'forward':
        hPos += int(dir[1])
    elif dir[0] == 'up':
        depth -= int(dir[1])
    elif dir[0] == 'down':
        depth += int(dir[1])

product = hPos * depth
print(product)


hPos = 0
depth = 0
aim = 0

for di in input:
    if di[0] == 'forward':
        hPos += int(di[1])
        depth += aim * int(di[1])
    elif di[0] == 'up':
        aim -= int(di[1])
    elif di[0] == 'down':
        aim += int(di[1])
        
print(hPos * depth)        
        