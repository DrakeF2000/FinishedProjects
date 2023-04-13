setCount = int(input())

output = []
for i in range(setCount):
    temp = []
    setOne = list(input())
    setTwo = list(input())
    for i in range(len(setOne)):
        if setOne[i] == setTwo[i]:
            temp.append(".")
        else:
            temp.append("*")
    output.append("".join(setOne))
    output.append("".join(setTwo))
    output.append("".join(temp))
    output.append(" ")

for i in range(len(output)):
    print(output[i])
