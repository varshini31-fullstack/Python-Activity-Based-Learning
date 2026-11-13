
print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")

# Getting product details
name = input("Enter product name: ")

quantity = int(input("Enter number of units manufactured: "))

material = float(input("Enter material cost per unit: "))

wastage = float(input("Enter wastage percentage: "))

labour = float(input("Enter labour cost per unit: "))

machine = float(input("Enter machine cost per unit: "))

selling_price = float(input("Enter selling price per unit: "))

target = float(input("Enter target profit percentage: "))

# Calculating material cost
material_cost = material * quantity

# Calculating wastage cost
wastage_cost = material_cost * wastage / 100

# Calculating labour cost
labour_cost = labour * quantity

# Calculating machine cost
machine_cost = machine * quantity

# Calculating total production cost
total_cost = material_cost + wastage_cost + labour_cost + machine_cost

# Calculating selling revenue
revenue = selling_price * quantity

# Calculating profit or loss
profit = revenue - total_cost

# Calculating profit percentage
profit_percent = (profit / total_cost) * 100

# Displaying manufacturing report
print("\n========== MANUFACTURING REPORT ==========")

print("Product Name:", name)
print("Quantity:", quantity)
print("Material Cost: Rs.", material_cost)
print("Wastage Cost: Rs.", wastage_cost)
print("Labour Cost: Rs.", labour_cost)
print("Machine Cost: Rs.", machine_cost)

print("------------------------------------------")

print("Total Production Cost: Rs.", total_cost)
print("Selling Revenue: Rs.", revenue)

if profit >= 0:
    print("Profit: Rs.", profit)
else:
    print("Loss: Rs.", abs(profit))

print("Profit Percentage:", round(profit_percent, 2), "%")

print("Target Profit:", target, "%")

# Checking profit target
if profit_percent >= target:
    print("Production meets the profit target.")
else:
    print("Production does not meet the profit target.")

print("==========================================")
