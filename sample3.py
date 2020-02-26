from math import factorial
a = list(map(int, input().split(",")))
for i in a:
    b = factorial(i)
    print(b, end = ",")
