initialInput = int(input())
numbers = input()
workingNumbers = numbers.split(" ")
output = 0
for _ in range(initialInput):
    if int(workingNumbers[_]) < 0:
        output += 1
print(output)