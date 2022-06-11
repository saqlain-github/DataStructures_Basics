def fib(n):
    if n <= 1:
        return n
    tmp = fib(n-1)+fib(n-2)
    print(n)
    return tmp

print(fib(8))