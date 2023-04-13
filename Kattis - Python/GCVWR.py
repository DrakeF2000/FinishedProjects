carInfo = list(map(int, input().split(" ")))
weightItems = list(map(int, input().split(" ")))
addedWeight = 0
for i in range(len(weightItems)):
    addedWeight += weightItems[i]
print(int((carInfo[0] - carInfo[1])*0.9 - addedWeight))