# RECURSION

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonaci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        a = 0
        b = 1
        for f in range(1, n):
            result = a + b
            a = b
            b = result
    return result
for i in range(36):
    print(i, fibonaci(i))

