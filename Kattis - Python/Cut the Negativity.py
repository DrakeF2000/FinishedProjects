size = int(input())

flights = []
row = 1
for i in range(size):
    data = list(map(int, input().split(" ")))
    for i in range(len(data)):
        if data[i] == -1:
            pass
        else:
            flights.append([row, i + 1, data[i]])
    row += 1
print(len(flights))
for i in range(len(flights)):
    print(flights[i][0], flights[i][1], flights[i][2])
