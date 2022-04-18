import random


def show_distribution(array, n):
    distArray = [0] * 4
    for i in range(n):
        if array[i] == 1:
            distArray[0] += 1
        elif array[i] == 2:
            distArray[1] += 1
        elif array[i] == 3:
            distArray[2] += 1
        else:
            distArray[3] += 1
    return distArray


def show_distribution2(array, n):
    distArray = [0] * 10
    for i in range(n):
        distArray[int(array[i]) % 10] += 1
    return distArray


def generate(n):
    array = []
    for _ in range(n):
        hazard = random.random()
        if hazard < 0.20:
            array.append(1)
        elif hazard < 0.60:
            array.append(2)
        elif hazard < 0.75:
            array.append(3)
        else:
            array.append(4)

    return show_distribution(array, n)


print(generate(100000))


def generate2(n):
    array = []
    for _ in range(n):
        hazard = random.random()
        array.append(100 * hazard + 50)
    return show_distribution2(array, n)

print(generate2(100000))