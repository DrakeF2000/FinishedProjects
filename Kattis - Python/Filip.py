data = list(map(int, input().split(" ")))
one = data[0]
two = data[1]
revOne = int(str(one)[::-1])
revTwo = int(str(two)[::-1])

if revOne > revTwo:
    print(revOne)
else:
    print(revTwo)
