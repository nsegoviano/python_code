def fibo(n):
    f = 0
    memo = {}
    
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fibo(n - 1) + fibo(n - 2)
    memo[n] = f
    print(memo)
    return f

a = fibo(8)
print(a)

