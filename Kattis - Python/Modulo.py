output = []
for i in range(10):
    num = int(input())
    temp = num % 42
    if temp in output:
        pass
    else:
        output.append(temp)
print(len(output))