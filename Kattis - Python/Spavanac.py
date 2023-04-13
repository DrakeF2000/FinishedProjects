inputList = input().split(" ")
hour = int(inputList[0])
minute = int(inputList[1])

if minute < 45:
    if hour != 00:
        hour -= 1
        minute += 15 
    else:
        if hour == 00:
            hour = 23
            minute += 15
        else:
            hour -= 1
            minute += 15
else:
    minute - 45

print(hour, minute)
