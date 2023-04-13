s = input()
output = []
for i in range(len(s)):
    if i <= len(s) - 2:
        if s[i] == ":" or s[i] == ";":
                if s[i + 1] == ")":
                    output.append(i)
                elif s[i + 1] == "-" and s[i + 2] == ")":
                    output.append(i)
for i in range(len(output)):
    print(output[i])