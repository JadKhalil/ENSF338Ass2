import timeit
import time
import matplotlib.pyplot as plt


def Memofunc(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = Memofunc(n-2) + Memofunc(n-1)
    return memo[n]


def func(n):
    if n == 1 or n == 0:
        return n
    return func(n-1) + func(n-2)


def PrintResults(memo, nonMemo):

    print("The following is the Time to execute the nonMemo fibonacci function for numbers 0-35")
    for i in range(len(nonMemo)):
        print("Time to compute Memofunc({}): {:.4f}".format(i, nonMemo[i]))

    print("")
    print("The following is the Time to execute the nonMemo fibonacci function for numbers 0-35")
    for i in range(len(memo)):
        print("Time to compute memo({}): {:.4f}".format(i, memo[i]))


def PlotResults(memo, nonMemo):

    xPoints = [i for i in range(len(memo))]

    plt.subplot(1, 2, 1)
    plt.plot(xPoints, memo)
    plt.title("Memoized function")
    plt.xlabel('function call argument')
    plt.ylabel('function call speed')

    plt.subplot(1, 2, 2)
    plt.plot(xPoints, nonMemo)
    plt.title("nonMemoized function")
    plt.xlabel('function call argument')
    plt.ylabel('function call speed')

    plt.show()


if __name__ == "__main__":

    nonMemoTime = []
    MemoTime = []
    for i in range(36):
        MemoTime.append(timeit.timeit(stmt='Memofunc(i)', setup='', timer=time.perf_counter,
                                      number=1, globals=globals()))

    for i in range(36):
        nonMemoTime.append(timeit.timeit(stmt='func(i)', setup='', timer=time.perf_counter,
                                         number=1, globals=globals()))

    PrintResults(MemoTime, nonMemoTime)
    PlotResults(MemoTime, nonMemoTime)
