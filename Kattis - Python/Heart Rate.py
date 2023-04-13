initialInput = int(input())
finalList = []
for _ in range(initialInput):
    initialGrab = input()
    workingSpace = initialGrab.split(" ")
    b = float(workingSpace[0])
    p = float(workingSpace[1])
    difference = 60 / p 
    BPM = 60 * b / p
    minABPM = BPM - difference
    maxABPM = BPM + difference
    finalList.append(f"{minABPM} {BPM} {maxABPM}")
for _ in range(initialInput):
    print(finalList[_])

