count = int(input())

area = 0
t1, v1 = map(float, input().split(" "))
for i in range(count - 1):
    t2, v2 = map(float, input().split(" "))
    temp = ((v1 + v2) / 2) * ((t2 - t1) / 1000)
    area += temp
    t1, v1 = t2, v2

print(area)