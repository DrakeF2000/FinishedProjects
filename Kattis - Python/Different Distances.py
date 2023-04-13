def func(x1, x2, y1, y2, p):
    first = abs(x1 - x2) ** p
    second = abs(y1 - y2) ** p
    temp = first + second
    out = temp ** (1/p)
    return out

output = []
while True:
    temp = input().split(" ")
    if len(temp) == 5:
        x1, y1, x2, y2, p = map(float, temp)
        output.append(func(x1, x2, y1, y2, p))
    else:
        break

for i in range(len(output)):
    print(output[i])
