def candles(n):
    sum = 0
    while n != 0:
        sum += n + 1
        n -= 1
    return sum


count = int(input())
output = []
for i in range(count):
    data = list(map(int, input().split(" ")))
    n = data[1]
    output.append(candles(n))

for i in range(len(output)):
    print(str(i + 1) + " " + str(output[i]))

