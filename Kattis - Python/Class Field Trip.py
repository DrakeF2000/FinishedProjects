nameOne = input()
nameTwo = input()
combinedNames = nameOne + nameTwo
workingNames = list(combinedNames)
workingNames.sort()
outputString = ''.join(workingNames)
print(outputString)