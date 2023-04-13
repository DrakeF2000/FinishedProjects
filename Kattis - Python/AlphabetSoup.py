initialInput = input()
totalcount = len(initialInput)
spacesCount = initialInput.count("_")
upperCaseCount = sum(1 for c in initialInput if c.isupper())
lowerCaseCount = sum(1 for c in initialInput if c.islower())

# Getting the ratios
spacesRatio = spacesCount / totalcount
upperRatio = upperCaseCount / totalcount
lowerRatio = lowerCaseCount / totalcount
symbolRatio = 1 - (spacesRatio + upperRatio + lowerRatio)

# Printing output
print(spacesRatio)
print(lowerRatio)
print(upperRatio)
print(symbolRatio)