import datetime
FILE_NAME = "expenses.txt"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (food, travel, bills, etc.): ")
    note = input("Optional note: ")
    date = datetime.date.today()
    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{amount},{category},{note}\n")
    print("Expense added successfully!\n")
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
        if not data:
            print("No expenses recorded yet.\n")
            return
        print("\n----- All Expenses -----")
        for line in data:
            date, amount, category, note = line.strip().split(",")
            print(f"Date: {date} | Amount: rupees {amount} | Category: {category} | Note: {note}")
        print()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")
def total_by_category():
    totals = {}
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
        if not data:
            print("No expenses to calculate.\n")
            return
        for line in data:
            date, amount, category, note = line.strip().split(",")
            amount = float(amount)
            totals[category] = totals.get(category, 0) + amount
        print("\n----- Total by Category -----")
        for category, total in totals.items():
            print(f"{category}: rupees {total:.2f}")
        print()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")
def main():
    while True:
        print("==== EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_by_category()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
if __name__ == "__main__":
    main()
