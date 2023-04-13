encrypt = input()
code = input()
data = [code[i:i+3] for i in range(0, len(code), 3)]
decrypt = []
for i in range(len(data)):
    decrypt.append(encrypt[int(data[i]) - 1])
print(''.join(decrypt))
