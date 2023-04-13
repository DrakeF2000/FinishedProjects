testCount = int(input())
output = []
for i in range(testCount):
    length = int(input())
    cities = []
    for i in range(length):
        city = input()
        if city not in cities:
            cities.append(city)
    output.append(len(cities))
for i in range(len(output)):
    print(output)
