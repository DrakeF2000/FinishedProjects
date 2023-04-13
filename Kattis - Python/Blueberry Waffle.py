r, f = map(int, input().split())

degrees = (f / r) * 180
data = degrees % 360

if data >= 0 and data <= 90:
    print("up")
elif data > 90 and data < 270:
    print("down")
elif data >= 270 and data <= 359:
    print("up")