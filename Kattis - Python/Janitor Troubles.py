import math
initialInput = input()
workableData = initialInput.split(" ")
firstPerimeter = 0
for value in range(4):
    firstPerimeter += int(workableData[value])

totalPerimeter = firstPerimeter / 2
a = totalPerimeter - int(workableData[0])
b = totalPerimeter - int(workableData[1])
c = totalPerimeter - int(workableData[2])
d = totalPerimeter - int(workableData[3])

underSquareValue = a * b * c * d
output = math.sqrt(underSquareValue)
print(output)