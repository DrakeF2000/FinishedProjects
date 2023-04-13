output = []
time = 0
count = 0
while count != -1:
    count = int(input())
    time = 0
    distance = 0
    for i in range(count):
        s, t = map(int, input().split(" "))
        timeDif = time - t
        distance += s * timeDif
        time = t
    output.append(abs(distance))

for i in range(len(output) - 1):
    print(str(output[i]) + " miles")
