count = 0
def tmp(n):
    if n>0:
        tmp(n-1)
        tmp(n-1)
        print("Recussion : ",n )

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

def factorial2(n,i):
    if i == 0:
        i == 1
    if i == n:
        return n
    return i*factorial2(n,i+1)



print(factorial(5))
print(factorial2(5,1))