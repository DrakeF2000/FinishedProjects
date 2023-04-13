input()
one = input().split(" ")
two = input().split(" ")

for i in range(len(two)):
    if two[i] in one:
        one.remove(two[i])
print(" ".join(one))