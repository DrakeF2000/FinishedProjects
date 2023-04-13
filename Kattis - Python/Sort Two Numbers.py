initialInput = input()
workingInput = initialInput.split(" ")
if workingInput[0] >= workingInput[1]:
    output = str(workingInput[1]) + " " + str(workingInput[0])
    print(output)
else:
    output = str(workingInput[0]) + " " + str(workingInput[1])
    print(output)