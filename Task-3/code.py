print("EMPLOYEE PAYROLL SYSTEM")

# Reading employee details
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

# Reading salary details
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

# Calculating overtime pay
overtime_pay = overtime_hours * overtime_rate

# Calculating gross salary
gross_salary = basic + allowances + overtime_pay + incentives

# Calculating deductions
if gross_salary <= 20000:
    deduction = gross_salary * 0.05
elif gross_salary <= 50000:
    deduction = gross_salary * 0.10
else:
    deduction = gross_salary * 0.15

# Calculating net salary
net_salary = gross_salary - deduction

# Displaying salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee Name       :", name)
print("Employee ID         :", emp_id)
print("--------------------------------------")
print("Basic Salary        : Rs.", basic)
print("Allowances          : Rs.", allowances)
print("Overtime Pay        : Rs.", overtime_pay)
print("Incentives          : Rs.", incentives)
print("--------------------------------------")
print("Gross Salary        : Rs.", round(gross_salary, 2))
print("Deduction           : Rs.", round(deduction, 2))
print("--------------------------------------")
print("Net Salary          : Rs.", round(net_salary, 2))
print("======================================")
