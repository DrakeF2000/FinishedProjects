initialInput = input()
workingData = initialInput.split(" ")
perfection = ["1", "1", "2", "2", "2", "8"]

outputString = ""
for _ in range(len(workingData)):
    if int(workingData[_]) != int(perfection[_]):
        outputString += str(int(perfection[_]) - int(workingData[_])) + " "
    else:
        outputString += "0" + " "
        
print(outputString)