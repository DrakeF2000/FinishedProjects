count = int(input())
output = []

for i in range(count):
    input()
    input()
    g = sorted(list(map(int, input().split(" "))))
    m = sorted(list(map(int, input().split(" "))))
    if max(g) >= max(m):
        output.append("Godzilla")
    else:
        output.append("MechaGodzilla")

for i in range(len(output)):
    print(output[i])
