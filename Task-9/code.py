print("CAMPUS EVENT FINANCIAL PLANNING")

# Reading fixed costs
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))

# Reading variable costs per participant
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

# Reading event details
participants = int(input("Enter number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculating fixed cost
fixed_cost = venue + equipment

# Calculating variable cost
variable_cost = catering + transport + certificate

# Calculating total variable cost
total_variable_cost = variable_cost * participants

# Calculating total event cost
total_cost = fixed_cost + total_variable_cost

# Calculating participant contributions
participant_contribution = registration_fee * participants

# Calculating total available funds
total_funds = participant_contribution + sponsorship

# Calculating profit or loss
profit_loss = total_funds - total_cost

# Calculating minimum registrations
if registration_fee > variable_cost:
    required = (fixed_cost - sponsorship) / (
        registration_fee - variable_cost
    )

    if required < 0:
        required = 0

    minimum_registrations = int(required)

    if minimum_registrations < required:
        minimum_registrations += 1

else:
    minimum_registrations = None

# Displaying financial report
print("\n========== EVENT FINANCIAL REPORT ==========")

print("Fixed Cost: Rs.", fixed_cost)
print("Variable Cost Per Participant: Rs.", variable_cost)
print("Total Variable Cost: Rs.", total_variable_cost)
print("Total Event Cost: Rs.", total_cost)

print("Participant Contributions: Rs.", participant_contribution)
print("Sponsorship Amount: Rs.", sponsorship)
print("Total Available Funds: Rs.", total_funds)

if profit_loss > 0:
    print("Profit: Rs.", profit_loss)

elif profit_loss < 0:
    print("Loss: Rs.", abs(profit_loss))

else:
    print("Event is at Break-Even Point")

if minimum_registrations is not None:
    print("Minimum Registrations Required:",
          minimum_registrations)
else:
    print("Break-even is not possible with the current registration fee.")

print("============================================")
