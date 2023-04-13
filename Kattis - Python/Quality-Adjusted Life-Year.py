periodsInLife = int(input())
outputValue = 0 
for _ in range(periodsInLife):
    termPeriod = input()
    splitTermPeriod = termPeriod.split()
    qualityOfLife = float(splitTermPeriod[0])
    yearsInPeriod = float(splitTermPeriod[1])
    outputValue += (qualityOfLife * yearsInPeriod)
print(outputValue)

    