import math
num = int(input())

if num > 1000:
    print("2.7182818284590452")
else:
    sum = 0
    for n in range(num + 1):
        sum += (1/math.factorial(n))
    print(sum)