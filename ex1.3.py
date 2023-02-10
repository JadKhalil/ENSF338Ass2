def Memofunc(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = Memofunc(n-2) + Memofunc(n-1)
    return memo[n]


print(Memofunc(200))
