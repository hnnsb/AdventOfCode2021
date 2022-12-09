from InputHandling import getdirabspath
import os
import ast

def getInput(day: str):
    path = getdirabspath()
    path_input = os.path.join(path, f'input {day}.txt')
    file = open(f'{path_input}', 'r')
    list = [x.strip() for x in file.readlines()]
    
    data = []
    for l in list:
        data.append(ast.literal_eval(l))

    return data
    

data = getInput('day18')



pass
