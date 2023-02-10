import sys
import timeit
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)


def readData():

    infile = open('data.csv', 'r')
    data = infile.read()

    intData = []

    for i in range(len(data)):
        if data[i] != ',' and data[i] != ' ':
            intData.append(data[i])

    return intData


def func1(arr, low, high):

    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def plotResult(timeA):

    xPoints = [i for i in range(len(timeA))]

    plt.plot(xPoints, timeA)
    plt.title("Memoized function")
    plt.xlabel('function call argument')
    plt.ylabel('function call speed')

    plt.show()


if __name__ == "__main__":
    data = readData()
    timeA = []
    n = 1

    for i in range(20):
        upper = i * n
        partitionedData = data[:upper+1]
        timeA.append(timeit.timeit(stmt='func1(partitionedData, i, upper)', setup='', timer=time.perf_counter,
                                   number=1, globals=globals()))
        n = n + 1

    plotResult(timeA)
