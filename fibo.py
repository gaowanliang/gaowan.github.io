from math import sqrt


def Fib(n):
    s = 5**(1/2)  # √5
    return int((1/s)*(((1+s)/2)**n - ((1-s)/2)**n))


for i in range(1, 100):
    # print(Fib(i))
    if(i >= 3):
        print(i, Fib(i))
