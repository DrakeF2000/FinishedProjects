initialInput = input()
wordLength = len(initialInput)
wordList = list(initialInput)
firstAPos = int(initialInput.find("a"))
output = []
for _ in range(wordLength):
    if firstAPos > _:
        pass
    else:
        output.append(wordList[_])
finalOutput = ''.join(output)
print(finalOutput)

