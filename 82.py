
n = int(input("Enter number of candidates: "))

candidates = []

for i in range(n):
    name = input("Enter candidate name: ")
    marks = int(input("Enter marks: "))
    score = int(input("Enter assessment score: "))
    attendance = int(input("Enter attendance percentage: "))

    if marks >= 60 and score >= 50 and attendance >= 75:
        candidates.append([name, marks, score])
    else:
        print(name, "is not eligible")
print("\nQualified Candidates Ranking:")

for i in range(len(candidates)):
    print(i + 1, candidates[i][0],
          "Marks:", candidates[i][1],
          "Score:", candidates[i][2])
