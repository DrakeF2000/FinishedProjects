health = list(map(int, input().split(" ")))
damage = list(map(int, input().split(" ")))

maxHealth = health[0]
attackCount = health[1]
potionCount = health[2]

curHealth = maxHealth
for i in range(len(damage)):
    if damage[i] >= curHealth and potionCount != 0:
        potionCount -= 1
        curHealth += 20
        if curHealth > maxHealth:
            curHealth = maxHealth
    curHealth -= damage[i]
if curHealth > 0:
    print("champion")
else:
    print("next time")