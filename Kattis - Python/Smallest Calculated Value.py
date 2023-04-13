initialInput = input()
dataList = initialInput.split(" ")
possibleAnswers = []
a = int(dataList[0])
b = int(dataList[1])
c = int(dataList[2])

one = (a + b) / c
two = (a + b) * c
three = (a + b) - c
four =(a + b) + c
five = (a - b) / c
six = (a - b) * c
seven = (a - b) - c
eight = (a - b) + c
nine = (a / b) / c
ten = (a / b) * c
eleven = (a / b) - c
tweleve = (a / b) + c
thirteen = (a * b) / c
fourteen = (a * b) * c
fifteen = (a * b) - c
sixteen = (a * b) + c

if type(one) != float:
    possibleAnswers.append(one)
possibleAnswers.append(two)
possibleAnswers.append(three)
possibleAnswers.append(four)
if type(five) != float:
    possibleAnswers.append(five)
possibleAnswers.append(six)
possibleAnswers.append(seven)
possibleAnswers.append(eight)
if type(nine) != float:
    possibleAnswers.append(nine)
if type(ten) != float:
    possibleAnswers.append(ten)
if type(eleven) != float:
    possibleAnswers.append(eleven)
if type(tweleve) != float:
    possibleAnswers.append(tweleve)
if type(thirteen) != float:
    possibleAnswers.append(thirteen)
possibleAnswers.append(fourteen)
possibleAnswers.append(fifteen)
possibleAnswers.append(sixteen)

answer = 100000000000
for _ in range(len(possibleAnswers)):
    if possibleAnswers[_ - 1] >= 0:
        if possibleAnswers[_ - 1] < answer:
            answer = possibleAnswers[_ - 1]
print(answer)
