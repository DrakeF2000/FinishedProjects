pointOne = list(map(int, input().split(" ")))
pointTwo = list(map(int, input().split(" ")))
pointThree = list(map(int, input().split(" ")))

xs = [pointOne[0], pointTwo[0], pointThree[0]]
ys = [pointOne[1], pointTwo[1], pointThree[1]]
outputx = 0
outputy = 0

for i in range(len(xs)):
    if xs.count(xs[i]) == 1:
        outputx = xs[i]
    if ys.count(ys[i]) == 1:
        outputy = ys[i]
print(str(outputx) + " " + str(outputy))