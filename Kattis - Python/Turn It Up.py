inputCounter = int(input())
temp = 7
for i in range(inputCounter):
    condition = input()
    if condition == "Skru op!":
        temp += 1
        if temp > 10:
            temp = 10
    if condition == "Skru ned!":
        temp -= 1
        if temp < 0:
            temp = 0
print(temp)