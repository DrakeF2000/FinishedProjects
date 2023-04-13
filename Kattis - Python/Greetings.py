# Greetings - Double the amount of e's from the intial input
initialInput = input()
eCount = initialInput.count('e')
addedEs = eCount * 2
heyList = ["h"]
for _ in range(addedEs):
    heyList.append('e')
heyList.append("y")
output = ''.join(heyList)
print(output)
