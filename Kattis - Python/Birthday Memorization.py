friendCount = int(input())
names = []
scores = []
dates = []

for i in range(friendCount):
    name, score, date = map(str, input().split())
    if date in dates:
        combatIndex = dates.index(date)
        combatScore = int(scores[combatIndex])
        if int(score) > combatScore:
            names[combatIndex] = name
            scores[combatIndex] = score
    elif date not in dates:
        names.append(name)
        scores.append(score)
        dates.append(date)
print(len(names))
sortedNames = sorted(names)
for i in range(len(sortedNames)):
    print(sortedNames[i])