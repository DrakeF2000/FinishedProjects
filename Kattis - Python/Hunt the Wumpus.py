initialSeed = int(input())
wumpiLocations = []

num = initialSeed
while len(wumpiLocations) != 4:
    gen = num + int(num/13) + 15
    genStr = str(gen)
    y = int(genStr[len(genStr) - 1])
    x = int(genStr[len(genStr) - 2])
    pos = (x, y)
    num = gen
    if pos in wumpiLocations:
        pass
    else:
        wumpiLocations.append(pos)


guessCount = 0
while len(wumpiLocations) != 0:
    userGuess = str(input())
    guessCount += 1
    userX = int(userGuess[0])
    userY = int(userGuess[1])
    userPos = (userX, userY)
    if userPos in wumpiLocations:
        wumpiLocations.remove(userPos)
        print("You hit a wumpus!")
    
    closest = 0
    distances = []
    for i in range(len(wumpiLocations)):
        distanceX = abs(userX - wumpiLocations[i][0])
        distanceY = abs(userY - wumpiLocations[i][1])
        distance = distanceX + distanceY
        distances.append(distance)
    for i in range(len(distances)):
        closest = min(distances)
    if closest != 0:
        print(closest)
print("Your score is " + str(guessCount) + " moves.")
