print("RAILWAY FARE AND RESERVATION SYSTEM")

# Reading journey details
n = int(input("Enter number of passengers: "))
distance = float(input("Enter journey distance in km: "))

total_fare = 0

# Processing each passenger
for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

    travel_class = input("Enter class (Sleeper/AC): ").lower()

    # Selecting fare rate
    if travel_class == "sleeper":
        rate = 1.5

    elif travel_class == "ac":
        rate = 3.0

    else:
        print("Invalid class. Please enter Sleeper or AC.")
        continue

    # Calculating basic fare
    basic_fare = distance * rate

    # Applying age concession
    if age < 5:
        basic_fare = 0

    elif age >= 60:
        basic_fare = basic_fare * 0.75

    # Adding reservation charge
    reservation = 50

    final_fare = basic_fare + reservation

    total_fare = total_fare + final_fare

    # Displaying passenger details
    print("\nPassenger Name:", name)
    print("Travel Class:", travel_class)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Reservation Charge: Rs.", reservation)
    print("Final Fare: Rs.", round(final_fare, 2))

# Displaying total fare
print("\n================================")
print("TOTAL RAILWAY FARE: Rs.", round(total_fare, 2))
print("================================")

# Cancellation calculation
choice = input("\nIs the ticket cancelled? (yes/no): ").lower()

if choice == "yes":

    penalty = total_fare * 0.25
    refund = total_fare - penalty

    print("\nCANCELLATION DETAILS")
    print("Total Fare: Rs.", round(total_fare, 2))
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Refund Amount: Rs.", round(refund, 2))

else:
    print("Ticket is confirmed.")
    print("Amount to be paid: Rs.", round(total_fare, 2))
