import numpy as np
import os

day = 'day01'
path = os.path.join(os.getcwd(), f'input {day}.txt')
file = open(path,'r')
inp = file.readlines()
file.close()


for i in range(len(inp)):
    inp[i]=int(inp[i].strip('\n'))


dec = 0
inc = 0
same = 0
for i in range(1,len(inp)):
    
    if inp[i-1] == inp[i]:
        same += 1
    elif inp[i-1] > inp[i]:
        dec += 1
    else:
        inc += 1

print(inc)

win = 3
count = 0
i = 0
while i in range(len(inp)) and i+win < len(inp):
    sumA = 0 
    for j in range(win): sumA +=inp[i+j]
    sumB = 0 
    for j in range(win): sumB +=inp[i+1+j]
    
    if sumA < sumB:
        count += 1
    
    i += 1
    
print(count)