import os

def main():
    data = getInput("day07")
    max = maximum(data)

    fuel1 = [[0 for _ in range(max + 1)] for __ in range(len(data))]
    fuel2 = [[0 for _ in range(max + 1)] for __ in range(len(data))]

    for i, crab in enumerate(data):
        fuel1[i][crab] = 0
        d = 0
        while crab - d >= 0 or crab + d < len(fuel1[0]):
            if crab - d >= 0:
                fuel1[i][crab - d] = d
                fuel2[i][crab - d] = fuelCostTask2(d)
            if crab + d < len(fuel1[0]):
                fuel1[i][crab + d] = d
                fuel2[i][crab + d] = fuelCostTask2(d)

            d += 1

    sumList1 = [] * (len(fuel1[0]) + 1)

    for i in range(len(fuel1[0])):
        sum1 = 0
        for j in range(len(fuel1)):
            sum1 += fuel1[j][i]

        sumList1.append(sum1)

    min1 = minimum(sumList1)

    sumList2 = [] * (len(fuel2[0]) + 1)

    for i in range(len(fuel2[0])):
        sum2 = 0
        for j in range(len(fuel2)):
            sum2 += fuel2[j][i]

        sumList2.append(sum2)

    min2 = minimum(sumList2)

    print(f'Part 1: {min1}')
    print(f'Part 2: {min2}')


def fuelCostTask2(index: int) -> int:
    return int(index * (index + 1) * (1 / 2))


def minimum(list: list[int]) -> int:
    min = 9999999999999999999999999999999
    for l in list:
        if l < min:
            min = l

    return int(min)


def maximum(list: list[int]) -> int:
    max = 0
    for l in list:
        if l > max:
            max = l

    return max


def getInput(day: str):
    path = os.path.join(os.getcwd(), f'{day}', f'input {day}.txt')
    file = open(f'{path}', 'r')
    raw = file.read().split(',')
    inp = [int(x) for x in raw]
    # print(inp)

    file.close()

    return inp


if __name__ == '__main__':
    main()
