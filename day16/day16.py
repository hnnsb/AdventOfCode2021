import sys
import os
import itertools
from copy import deepcopy
from collections import defaultdict, Counter
from typing import Counter, Tuple
sys.setrecursionlimit(int(1e6))


def getInput(day: str):
    path_self = os.path.dirname(os.path.abspath('__file__'))
    path_input = os.path.join(path_self, f'{day}', f'input {day}.txt')
    file = open(f'{path_input}', 'r')
    raw = file.readline()
    # inp = [line.strip('\n').split(' -> ') for line in raw]
    return raw


print('Part1')
data = getInput('day16')
# data = 'C0015000016115A2E0802F182340'
bits = ''
for c in data:
    num = int(c, 16)
    bits += format(num, '04b')

pos = 0
res = 0
sum_of_versions = 0


def parse(bits, pos, depth):
    global sum_of_versions
    version = int(bits[pos:pos+3], 2)  # 3 chars long
    sum_of_versions += version
    typeID = int(bits[pos+3:pos+6], 2)  # 3 chars long

    if typeID == 4:  # Packet content is a literal
        # interpret literal

        pos += 6
        v = 0
        while True:
            v = v*16 + int(bits[pos+1:pos+5],2)
            pos += 5
            if bits[pos-5] == '0':
                return v, pos
    else:  # Packet content is not a literal
        versions = []

        lengthType = int(bits[pos+6], 2)  # 1 char long
        # Interpret the lengthType
        if lengthType == 0:
            length = 15
            len_bits = int(bits[pos+7:pos+7+length], 2)
            start_pos = pos + 7 + length # Shift position according to length of content
            pos = start_pos
            while True:
                v, next_pos = parse(bits, pos, depth + 1)
                versions.append(v)
                pos = next_pos
                if next_pos - start_pos == len_bits:
                    break

        else:
            length = 11
            n_packets = int(bits[pos+7:pos+7+length], 2)
            pos += 7+length

            for t in range(n_packets):
                v, next_pos = parse(bits, pos, depth + 1)
                versions.append(v)
                pos = next_pos
           
        if typeID == 0:
            return sum(versions), pos
        elif typeID == 1:
            ans = 1
            for v in versions:
                ans *= v
            return ans, pos
        elif typeID == 2:
            return min(versions), pos
        elif typeID == 3:
            return max(versions), pos
        elif typeID == 5:
            return (1 if versions[0] > versions[1] else 0), pos
        elif typeID == 6:
            return (1 if versions[0] < versions[1] else 0), pos
        elif typeID == 7:
            return (1 if versions[0] == versions[1] else 0), pos

value, next_pos = parse(bits, 0,0)

print(sum_of_versions)

print('Part2')
print(value)