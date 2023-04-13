initialInput = int(input())
stringsGiven = []
for word in range(initialInput):
    stringsGiven.append(input())
for wordNum in range(initialInput):
    if int(wordNum) % 2 == 0:
        print(stringsGiven[wordNum])
