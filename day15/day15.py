import os
import heapq
import itertools
from copy import deepcopy
from collections import defaultdict, Counter
from typing import Counter, Tuple


def getInput(day: str):
    path_self = os.path.dirname(os.path.abspath('__file__'))
    path_input = os.path.join(path_self, f'{day}', f'input {day}.txt')
    file = open(f'{path_input}', 'r')
    raw = file.readlines()
    raw = [l.strip('\n') for l in raw]
    d = [[int(x) for x in line]for line in raw]
    # inp = [line.strip('\n').split(' -> ') for line in raw]
    return d


G = getInput('day15')
matrix = getInput('day15')

lenX = len(matrix[0])
lenY = len(matrix)
distance = {}

# print('Part 1:')


print('Part 2:')






R = len(G)
C = len(G[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def solve(n_tiles):
    D = [[None for _ in range(n_tiles*C)] for _ in range(n_tiles*R)]
    Q = [(0,0,0)]
    while Q:
        (dist,r,c) = heapq.heappop(Q)
        if r<0 or r>=n_tiles*R or c<0 or c>=n_tiles*C:
            continue

        val = G[r%R][c%C] + (r//R) + (c//C)
        while val > 9:
            val -= 9
        rc_cost = dist + val

        if D[r][c] is None or rc_cost < D[r][c]:
            D[r][c] = rc_cost
        else:
            continue
        if r==n_tiles*R-1 and c==n_tiles*C-1:
            break

        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            heapq.heappush(Q, (D[r][c],rr,cc))
    return D[n_tiles*R-1][n_tiles*C-1] - G[0][0]

print(solve(1))
print(solve(5))