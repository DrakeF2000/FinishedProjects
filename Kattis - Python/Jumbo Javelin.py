initialInput = int(input())
rod_lengths = []
for rod in range(initialInput):
    rod_lengths.append(input())
output = 0
for rod in range(initialInput):
    if rod == 0:
        output += int(rod_lengths[rod])
    else:
        output += int(rod_lengths[rod]) - 1
print(output)
