output = []
while True:
    n, d = map(int, input().split(" "))

    if n == 0 and d == 0:
        break
    
    quotient = n // d
    remainder = n % d

    output.append(f"{quotient} {remainder} / {d}")

for i in range(len(output)):
    print(output[i])