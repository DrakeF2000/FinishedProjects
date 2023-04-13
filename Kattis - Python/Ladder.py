import math
h, v = map(int, input().split(" "))

radians = v * math.pi / 180
test = math.ceil(h / math.sin(radians))
print(test)