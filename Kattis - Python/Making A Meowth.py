n, p, x, y = map(int, input().split(" "))
time = 0
time += (p * x)
meowth = 0
while p > 0:
    p -= (n - 1)
    if p < 0:
        pass
    else:
        meowth += 1
time += meowth * y
print(time)