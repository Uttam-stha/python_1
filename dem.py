def rent_calculator():
    print("=== Rent Calculator ===")

    rent = float(input("Enter monthly rent(NRP):"))

    electricity = float(input("Enter monthly electricity bill (NRP):"))
    water = float(input("Enter monthly water bill(NRP):"))
    internet = float(input("Enter monthly internet bill (NRP):"))

    other = float(input("Enter other monthly expenses (NRP):"))

    total_monthly = rent + electricity + water + internet + other
    print(f"Total Monthly Cost: NRP {total_monthly:.2f}")

    total_yearly = total_monthly * 12
    print(f"Total Yearly Cost:NRP {total_yearly:.2f}")

    roommates = int(input("\nEnter number of roommates (including you):"))
    if roommates > 0:
        per_person = total_monthly / roommates
        print(f"Each person pats: NRP {per_person:.2f} per month")

rent_calculator()