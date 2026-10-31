print("Semester Progression Eligibility")

marks = int(input("Enter semester marks: "))
attendance = int(input("Enter attendance percentage: "))
subjects = int(input("Enter number of subjects: "))
passed = int(input("Enter number of subjects passed: "))
prerequisite = input("Are prerequisites completed? (yes/no): ").lower()

if marks < 0 or marks > 100:
    print("Invalid marks")
elif attendance < 0 or attendance > 100:
    print("Invalid attendance")
elif subjects <= 0 or passed < 0 or passed > subjects:
    print("Invalid subject details")
else:
    eligible = True

    if marks < 40:
        print("Outstanding requirement: Minimum 40 marks needed")
        eligible = False

    if attendance < 75:
        print("Outstanding requirement: Minimum 75% attendance needed")
        eligible = False

    if passed < subjects:
        print("Outstanding requirement: Pass all subjects")
        eligible = False

    if prerequisite != "yes":
        print("Outstanding requirement: Complete prerequisites")
        eligible = False

    if eligible:
        print("Eligible for next semester")
    else:
        print("Not eligible for next semester")