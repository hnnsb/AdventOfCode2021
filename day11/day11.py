def getInput(path):
    file = open(f'{path}', 'r')
    raw = file.readlines()
    raw = [x.strip('\n') for x in raw]

    inp = [[int(x.strip('\n')) for x in row] for row in raw]

    file.close()

    return inp


def flash(x, y, data, flashed):
    if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data):
        data[y][x] += 1
        if not flashed[y][x] and data[y][x] > 9:
            flashed[y][x] = True
            data[y][x] = 0

            flash(x-1, y-1, data, flashed)
            flash(x, y-1, data, flashed)
            flash(x+1, y-1, data, flashed)
            flash(x-1, y, data, flashed)
            flash(x+1, y, data, flashed)
            flash(x-1, y+1, data, flashed)
            flash(x, y+1, data, flashed)
            flash(x+1, y+1, data, flashed)
        else:
            return


def didAllFlash(flashed):
    for y, row in enumerate(flashed):
        for x, cell in enumerate(row):
            if not cell:
                return False

    return True

data = getInput("day11/input day11.txt")

# data = [[1, 1, 1, 1, 1],
#         [1, 9, 9, 9, 1],
#         [1, 9, 1, 9, 1],
#         [1, 9, 9, 9, 1],
#         [1, 1, 1, 1, 1]]

flashes = 0
days = 1000
allFlash = 0

for day in range(days):
    flashed = [[False for _ in range(10)] for __ in range(10)]

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            flash(x, y, data, flashed)

    # sum flashes
    for y, row in enumerate(flashed):
        for x, cell in enumerate(row):
            if cell:
                data[y][x] = 0
                flashes += 1

    if didAllFlash(flashed):
        print('Part 2: \nall flashed on day: ')
        print(day+1) # day is off by one, not sure why
        break

    if day == 99:
        print('part1: \nFlashes after 100 steps')
        print(flashes)
