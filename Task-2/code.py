students = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")

    subjects = int(input("Enter number of subjects: "))

    marks = []

    for j in range(subjects):
        mark = float(input("Enter marks in subject " + str(j + 1) + ": "))
        marks.append(mark)

    aggregate = sum(marks) / subjects

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    if (aggregate >= 80 and min(marks) >= 60
            and attendance >= 75 and income <= 200000):

        students.append([name, aggregate, attendance, income])

students.sort(key=lambda x: (-x[1], -x[2], x[3]))

if len(students) == 0:
    print("\nNo eligible students found.")
else:
    print("\nEligible Students Ranked by Scholarship Priority")
    

    for i, student in enumerate(students):
        print("\nRank:", i + 1)
        print("Name:", student[0])
        print("Aggregate:", round(student[1], 2), "%")
        print("Attendance:", student[2], "%")
        print("Family Income: Rs.", student[3])
