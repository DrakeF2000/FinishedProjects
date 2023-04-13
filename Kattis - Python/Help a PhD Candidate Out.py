count = int(input())

output = []
for i in range(count):
    data = input()
    if data == "P=NP":
        output.append("skipped")
    else:
        temp = data.replace("+", " ")
        a, b = map(int, temp.split(" "))
        output.append(a + b)

for i in range(len(output)):
    print(output[i])