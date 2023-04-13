e, f, c = map(int, input().split(" "))

bottles = e + f
drank = 0
while bottles >= c:
    new_bottles = bottles // c
    bottles = bottles % c + new_bottles
    drank += new_bottles

print(drank)