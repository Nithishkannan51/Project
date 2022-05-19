def printPascal(n):
    # Iterate through every line
    # and print entries in it
    for line in range(0, n):

        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line+1):
            print(binomialCoeff(line, i),
                  " ", end="")
        print()



def binomialCoeff(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res


# Driver program
n = 7
printPascal(n)

n = 5
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='')
    for k in range(0,2*i+1):
        print("*",end='')
    print()
for i in range(n-1,0,-1):
    for j in range(n,i,-1):
        print(" ",end='')
    for k in range(2*i-1,0,-1):
        print("*",end='')
    print()

n = 5
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(i, n):
        if (j == i or i == 0 or j == n - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()

row =5

for i in range(row):
    for j in range(row - i):
        print(' ', end='')  # printing space required and staying in same line

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == row - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()  # printing new line