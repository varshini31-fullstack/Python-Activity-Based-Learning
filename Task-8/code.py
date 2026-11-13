print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

# Defining exchange rates
rates = {
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}

# Reading travel budget
budget = float(input("Enter travel budget in INR: "))

n = int(input("Enter number of expense categories: "))

expenses = {}
total_expense = 0

# Processing travel expenses
for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    currency = input("Enter currency (USD/EUR/GBP): ").upper()
    amount = float(input("Enter expense amount: "))

    if currency in rates:

        # Converting currency into INR
        converted = amount * rates[currency]

        # Calculating conversion fee
        fee = converted * 0.02

        # Calculating final expense
        final_amount = converted + fee

        expenses[category] = final_amount
        total_expense += final_amount

        print("Converted Amount: Rs.", round(converted, 2))
        print("Conversion Fee: Rs.", round(fee, 2))
        print("Final Expense: Rs.", round(final_amount, 2))

    else:
        print("Invalid currency! Expense not included.")

# Finding largest expense category
if len(expenses) > 0:
    largest_category = max(expenses, key=expenses.get)
    largest_amount = expenses[largest_category]
else:
    largest_category = "None"
    largest_amount = 0

# Displaying final report
print("\n========== TRAVEL BUDGET REPORT ==========")

for category, amount in expenses.items():
    print(category, ": Rs.", round(amount, 2))

print("------------------------------------------")

print("Total Travel Expense: Rs.", round(total_expense, 2))
print("Available Budget: Rs.", round(budget, 2))

# Comparing expenses with budget
if total_expense <= budget:
    print("Budget Status: Within Budget")
    print("Remaining Amount: Rs.",
          round(budget - total_expense, 2))
else:
    print("Budget Status: Budget Exceeded")
    print("Extra Amount Required: Rs.",
          round(total_expense - budget, 2))

print("------------------------------------------")

print("Largest Expense Category:", largest_category)
print("Largest Expense Amount: Rs.", round(largest_amount, 2))

print("==========================================")
