s = input()
words = list(s.split(" "))

output = []
for i in range(len(words)):
    for j in range(0, len(words)):
        if words[j]==words[i] and i !=j:
            output.append(1)
if len(output) != 0:
    print("no")
else:
    print("yes")