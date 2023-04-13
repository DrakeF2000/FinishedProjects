initialInput = input()
workingList = initialInput.split(" ")
fizz = int(workingList[0])
buzz = int(workingList[1])
loopEnd = int(workingList[2])

outputList = []
for _ in range(1, loopEnd + 1):
    if _ % fizz == 0 and _ % buzz == 0:
        outputList.append("FizzBuzz")
    else:
        if _ % fizz == 0:
            outputList.append("Fizz")
        elif _ % buzz == 0:
            outputList.append("Buzz")
        else:
            outputList.append(_)

for _ in range(0, len(outputList)):
    print(outputList[_])
        