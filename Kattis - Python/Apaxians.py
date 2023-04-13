name = list(input())

output = []
output.append(name[0])
for i in range(len(name)):
    if i != 0:
        if name[i] == name[i - 1]:
            pass
        else:
            output.append(name[i])

print("".join(output))
