import math

def factor(a):
    mid = int(math.sqrt(a))
    for i in range(int(mid*1.1), 0, -1):
        if a % i == 0:
            j = a/i
            print("%d, %d" % (i, j))
            return


def gcd(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b


