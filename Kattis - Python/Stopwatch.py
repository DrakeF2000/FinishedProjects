loopLength = int(input())
timeData = []
stopWatchTime = 0
for i in range(loopLength):
    timeData.append(int(input()))
if loopLength % 2 == 1:
    print("still running")
else:
    count = 0
    while count != loopLength:
        count += 2
        stopWatchTime += (timeData[count] - timeData[count - 1])
    print(stopWatchTime)
