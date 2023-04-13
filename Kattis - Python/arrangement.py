lineCount = int(input())
starCount = int(input())
outputList = []

for _ in range(lineCount):
    outputList.append("*")
starCount -= lineCount
while starCount != 0:
    for _ in range(len(outputList)):
        outputList[_ - 1].append("*")
        starCount -= 1
print(outputList)