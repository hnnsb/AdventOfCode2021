import os
from collections import defaultdict

def getInput(day: str):
    path = os.path.join(os.getcwd(), f'input {day}.txt')

    file = open(f'{path}', 'r')
    raw = file.readlines()
    inp = [x.strip('\n') for x in raw]
    edges = [x.split('-') for x in inp]
    nodes = set()
    for edge in edges:
        for node in edge:
            if node not in nodes:
                nodes.add(node)

    file.close()

    return edges, nodes


edges, nodes = getInput('day12')

adj = defaultdict(list)
for edge in edges:
    a,b = edge[0], edge[1]
    adj[a].append(b)
    adj[b].append(a)

# print(edges)
# print(nodes)
# print(visited)
paths = set()
res = 0
start = ('start', set(['start']), None)
stack = [start]
while stack:
    pos, small, twice = stack.pop()
    if pos == 'end':
        res += 1
        continue

    for n in adj[pos]:
        if n not in small:
            small_new = set(small)
            if n.islower():
                small_new.add(n)
            
            stack.append((n, small_new, twice))
        # elif n in small and twice is None and n not in ['start','end']: # Part 2
        #     stack.append((n,small,n))

print(res)