import statistics
dayCount = int(input())
runner1 = list(map(int, input().split(" ")))
runner2 = list(map(int, input().split(" ")))
runner3 = list(map(int, input().split(" ")))

output = []
for i in range(dayCount):
    data = [runner1[i], runner2[i], runner3[i]]
    distance = statistics.median(data)
    output.append(str(distance))
print(" ".join(output))
