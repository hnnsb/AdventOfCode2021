import os

def getInput(day: str):
    path = os.path.join(os.getcwd(), f'{day}', f'input {day}.txt')
    file = open(f'{path}', 'r')
    raw = file.readlines()

    inp = [x.strip('\n') for x in raw]

    file.close()

    return inp


data = getInput('day10')

open = ['(', '[', '{', '<']
close = [')', ']', '}', '>']

otc = {'(': ')', '[': ']', '{': '}', '<': '>'}

illegal = {')': 3, ']': 57, '}': 1197, '>': 25137}
correc = {'(': 1, '[': 2, '{': 3, '<': 4}

score1 = 0
scores = []

for row in data:
    l = []
    corrupted = False
    score2 = 0
    for c in row:
        if c in open:
            l.append(c)

        if c in close:
            if c == otc[l[-1]]:
                l.pop()
            else:
                # print(row, ' corrupted at', c)
                score1 += illegal[c]
                corrupted = True
                break

    if not corrupted:
        l.reverse()
        for p in l:
            score2 = score2 * 5
            score2 += correc[p]

        scores.append(score2)

print('Part 1:')
print(score1)

print('Part 2:')
scores.sort()
print(scores[int(len(scores)/2)])
