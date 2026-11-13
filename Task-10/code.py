print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")

# Reading student details
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

# Initializing variables
total = 0
total_grace = 0
all_pass = True

pass_mark = 40
max_marks = 100
grace_limit = 5

subjects = []

# Processing subject marks
for i in range(n):

    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")

    marks = float(input("Enter marks obtained: "))

    # Validating marks
    while marks < 0 or marks > max_marks:
        print("Invalid marks! Enter marks between 0 and 100.")
        marks = float(input("Enter marks again: "))

    grace = 0

    # Checking pass criteria
    if marks < pass_mark:

        shortage = pass_mark - marks

        # Applying grace marks
        if shortage <= grace_limit:
            grace = shortage
            marks = min(marks + grace, max_marks)

        else:
            all_pass = False

    # Checking final pass status
    if marks < pass_mark:
        all_pass = False

    # Updating total marks
    total += marks
    total_grace += grace

    subjects.append((subject, marks, grace))

# Calculating percentage
percentage = (total / (n * max_marks)) * 100

# Determining classification
if all_pass:

    if percentage >= 75:
        classification = "Distinction"

    elif percentage >= 60:
        classification = "First Class"

    elif percentage >= 50:
        classification = "Second Class"

    else:
        classification = "Pass"

    result = "PASS"

else:
    result = "FAIL"
    classification = "No Classification"

# Displaying final result
print("\n========== EXAMINATION RESULT ==========")

print("Student Name:", name)

print("\nSubject-wise Marks:")

for subject, marks, grace in subjects:
    print(subject, ":", marks,
          "| Grace Marks:", grace)

print("----------------------------------------")

print("Total Marks:", total)
print("Maximum Marks:", n * max_marks)
print("Total Grace Marks:", total_grace)
print("Percentage:", round(percentage, 2), "%")
print("Final Result:", result)
print("Classification:", classification)

print("========================================")
