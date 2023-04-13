numHits = int(input())
hits = list(map(int, input().split(" ")))
points = 0
hitsCounted = 0
for i in range(len(hits)):
    if hits[i] != -1:
        points += hits[i]
        hitsCounted += 1
baseAverage = points / hitsCounted
print(baseAverage)
