import os

# def getInput(day: str):
#     path_self = os.path.dirname(os.path.abspath('__file__'))
#     path_input = os.path.join(path_self, f'{day}', f'input {day}.txt')
#     file = open(f'{path_input}', 'r')
#     raw = file.readline()
#     # inp = [line.strip('\n').split(' -> ') for line in raw]
#     return raw

# data = getInput('day17')

# target area: x=139..187, y=-148..-89

yOffset = +150

coor = [[' ' for _ in range(200)] for __ in range (300)]

for y in range(yOffset + 89, yOffset +  148 + 1):
    for x in range(139,187+1):
        coor[y][x] = 'T'

coor[0+yOffset][0] = 'S'



def draw(coor):
    for i,row in enumerate(coor):
        line = ''
        for y in row:
            line += y
        print(i, ': ', line)


def inTarget(x,y):
    if x in range(139,187+1) and y in range(yOffset + 89, yOffset +  148 + 1):
        return True
    else: return False


def shoot(xVel,yVel):
    hit = False
    x = 0
    y = yOffset
    h = []
    while True:
        x += xVel
        y -= yVel
        if xVel > 0:
            xVel -= 1
        elif xVel < 0:
            xVel += 1

        yVel -= 1

        if y > 300:
            break
        
        h.append(y-yOffset)
        try:
            if y >= 0 and x >= 0:
                coor[y][x] = '#'
        except:
            continue

        if inTarget(x,y):
            hit = True
            # print('hit')
            break
    
    # print(min(h))
    height = -1*min(h)
    return hit, height


# print('Part1')
# hits = 0
# for i in range(20):
#     for j in range(200):
#         hit, height = shoot(i,j)
#         if hit:
#             if hits < height:
#                 hits = height
#             print (f'Velocities: x: {i}, y: {j} reach the height {height} and hit the target')

# print('max reached height is' , hits)

print('Part 2:')
count = 0
for i in range(200):
    for j in range(-150,500):
        hit, height = shoot(i,j)
        if hit:
            count += 1
            # print (f'Velocities: x: {i}, y: {j} hit the target')

print(f'There are {count} different options')