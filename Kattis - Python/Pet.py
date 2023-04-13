score = 0
winner = 0
for contestant in range(1, 6):
    grades = [int(x) for x in input().split(" ")]
    contestantScore = sum(grades)
    if contestantScore > score:
        winner = contestant 
        score = contestantScore
print(winner, score)