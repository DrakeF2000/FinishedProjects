initialInput = int(input())
numbers = input()
numbersSplit = numbers.split(" ")
output = 0
for num in range(initialInput):
    output += int(numbersSplit[num - 1])
print(output)
