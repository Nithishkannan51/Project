#Q1

def twicemuliply(func):
    def inner(a, b):
        func(a,b)
        func(a, b)

    return inner

@twicemuliply
def multiply(a, b):
    print(a*b)

multiply(2,3)

#Q2
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("Enter Fibonacci series limit")
n=int(input())
x = fib(n)
for i in fib(n):
    print(i)