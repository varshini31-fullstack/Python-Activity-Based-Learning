EXPERIMENT 1: UNIVERSITY SCHOLARSHIP ALLOCATION
1. Problem Statement
Design a Python program to evaluate students for scholarships based on aggregate marks, minimum subject marks, attendance percentage, and annual family income. The program should identify eligible students, rank them according to aggregate marks, and resolve ties using attendance and lower family income.
2. Algorithm
1. Start.
2. Read the number of students.
3. Create an empty list to store eligible students.
4. Read each student's name, aggregate marks, subject marks, attendance, and family income.
5. Check the eligibility conditions:
   - Aggregate marks >= 80.
   - Subject marks >= 60.
   - Attendance >= 75%.
   - Family income <= ₹2,00,000.
6. If all conditions are satisfied, add the student to the list.
7. Sort eligible students by aggregate marks, attendance, and family income.
8. Display the ranked list.
9. Stop.
3. ##Flowchart (Mermaid)
   ~~~ mermaid
    A([Start]) --> B[/Enter number of students/]
    B --> C[Initialize eligible list]
    C --> D[/Enter student details/]
    D --> E{Marks >= 80 and Subject >= 60?}
    E -->|Yes| F{Attendance >= 75 and Income <= 200000?}
    E -->|No| H{More students?}
    F -->|Yes| G[Add student to eligible list]
    F -->|No| H
    G --> H
    H -->|Yes| D
    H -->|No| I[Sort eligible students]
    I --> J[/Display student rankings/]
    J --> K([Stop])
   ~~~

5. Sample Input
Enter number of students: 3

Student 1
Enter name: Ravi
Enter aggregate marks: 85
Enter subject marks: 70
Enter attendance: 90
Enter family income: 150000

Student 2
Enter name: Priya
Enter aggregate marks: 92
Enter subject marks: 80
Enter attendance: 95
Enter family income: 180000

Student 3
Enter name: Arun
Enter aggregate marks: 75
Enter subject marks: 65
Enter attendance: 80
Enter family income: 100000

6. Sample Output
Scholarship Eligible Students

1 Priya Marks: 92.0 Attendance: 95.0 Income: 180000.0
2 Ravi Marks: 85.0 Attendance: 90.0 Income: 150000.0
