
# 📌 Rent Calculator Project
# ============================

def rent_calculator():
    print("=== Rent Calculator ===")

    # Step 1: Input monthly rent
    rent = float(input("Enter monthly rent (NPR): "))

    # Step 2: Input utilities
    electricity = float(input("Enter monthly electricity bill (NPR): "))
    water = float(input("Enter monthly water bill (NPR): "))
    internet = float(input("Enter monthly internet bill (NPR): "))

    # Step 3: Other expenses
    other = float(input("Enter other monthly expenses (NPR): "))

    # Step 4: Total monthly cost
    total_monthly = rent + electricity + water + internet + other
    print(f"\nTotal Monthly Cost: NPR {total_monthly:.2f}")

      # Step 5: Yearly cost
    total_yearly = total_monthly * 12
    print(f"Total Yearly Cost: NPR {total_yearly:.2f}")

    # Step 6: Split among roommates
    roommates = int(input("\nEnter number of roommates (including you): "))
    if roommates > 0:
        per_person = total_monthly / roommates
        print(f"Each person pays: NPR {per_person:.2f} per month")

# Run the calculator
rent_calculator()