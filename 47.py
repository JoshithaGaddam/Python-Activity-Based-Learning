
n = int(input("Enter number of teams: "))

teams = []

for i in range(n):
    name = input("Enter team name: ")
    wins = int(input("Enter wins: "))
    draws = int(input("Enter draws: "))
    goals = int(input("Enter goal difference: "))

    points = wins * 3 + draws
    teams.append([name, points, goals])
print("\nTournament Rankings:")
for i in range(n):
    print(i + 1, teams[i][0],
          "Points:", teams[i][1],
          "Goal Difference:", teams[i][2])
