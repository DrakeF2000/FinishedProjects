initialInput = int(input())
taxInput = input()
taxInfo = taxInput.split(" ")
totalExpenses = 0
for tax in range(initialInput):
    if int(taxInfo[tax]) < 0:
        totalExpenses += int(taxInfo[tax])
output = totalExpenses * -1
print(output)