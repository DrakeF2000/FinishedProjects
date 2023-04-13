initialInput = int(input())
outputList = []
for _ in range(initialInput):
    values = input()
    valueList = values.split(" ")
    numberOfCords = int(valueList[0])
    workingTotal = 0
    for _ in range(numberOfCords + 1):
        if _ == 0:
            pass
        elif _ > 0:
            workingTotal += int(valueList[_])
    toOutputList = workingTotal - numberOfCords + 1
    outputList.append(toOutputList)
for _ in range(initialInput):
    print(outputList[_])