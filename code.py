print("MOBILE PLAN COST OPTIMIZATION")

# Available mobile plans
plans = [
    ["Basic", 199, 100, 28],
    ["Standard", 299, 200, 28],
    ["Premium", 399, 300, 56]
]

# Reading user requirements
usage = float(input("Enter your data usage in GB: "))
validity = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget: "))

eligible_plans = []

# Checking each plan
for plan in plans:

    name = plan[0]
    price = plan[1]
    data_limit = plan[2]
    days = plan[3]

    # Calculate excess data and charges
    excess_data = max(0, usage - data_limit)
    excess_charge = excess_data * 10

    total_cost = price + excess_charge

    # Check plan eligibility
    if days >= validity and total_cost <= budget:

        eligible_plans.append([
            name, total_cost, data_limit, days, excess_data
        ])

# Displaying the result
if len(eligible_plans) == 0:

    print("\nNo suitable mobile plan found within your budget.")

else:

    # Sort plans by total cost
    eligible_plans.sort(key=lambda x: x[1])

    best_plan = eligible_plans[0]

    print("\n===== MOST ECONOMICAL MOBILE PLAN =====")
    print("Plan Name       :", best_plan[0])
    print("Total Cost      : Rs.", best_plan[1])
    print("Data Limit      :", best_plan[2], "GB")
    print("Validity        :", best_plan[3], "days")
    print("Excess Data     :", best_plan[4], "GB")

    print("\n===== OTHER ELIGIBLE PLANS =====")

    for plan in eligible_plans:
        print(plan[0], "- Rs.", plan[1])
