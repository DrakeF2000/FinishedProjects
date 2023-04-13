data = input().replace(";", " ").split(" ")

count = 0
for i in range(len(data)):
    if "-" in data[i]:
        temp = data[i].replace("-", " ").split(" ")
        one = int(temp[0])
        two = int(temp[1])
        count += two - one + 1
    else: count += 1
print(count)