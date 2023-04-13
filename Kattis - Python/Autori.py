names = input()
dataList = names.split("-")
outputList = []
for _ in range(len(dataList)):
    outputList.append(dataList[_][0])
output = ''.join(outputList)
print(output)