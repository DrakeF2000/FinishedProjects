testCount = int(input())

output = []
for i in range(testCount):
    a, b, c = map(int, input().split(" "))
    temp = []
    temp.append(a + b)
    temp.append(a - b)
    temp.append(a * b)
    temp.append(a / b)
    temp.append(b - a)
    temp.append(b / a)
    if c in temp:
        output.append("Possible")
    else: output.append("Impossible")
for i in range(len(output)):
    print(output[i])
