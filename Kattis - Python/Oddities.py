loopLength = int(input())
output = []
for i in range(loopLength):
    integer = int(input())
    if integer % 2 == 0:
        output.append(str(integer) + " is even")
    else:
        output.append(str(integer) + " is odd")
for i in range(loopLength):
    print(output[i])