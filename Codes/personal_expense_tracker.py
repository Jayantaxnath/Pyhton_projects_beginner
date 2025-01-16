# Project_01
import os

# File to store expense data
expense_file = "expenses.txt"

# The file exists or not
if not os.path.exists(expense_file):
    open(expense_file, "w").close()

def add_expense():
    """Add a new expense."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    amount = input("Enter the amount: ")
    description = input("Enter a description: ")
    with open(expense_file, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")
    print("Expense added successfully!")


def view_expenses():
    """View all expenses."""
    print("\nYour Expenses:")
    if os.stat(expense_file).st_size == 0:
        print("No expenses found.")
        return
    with open(expense_file, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            print(f"Date: {date}, Category: {category}, Amount: {amount}, Description: {description}")
    print()


def delete_expense():
    """Delete an expense."""
    view_expenses()
    date_to_delete = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    with open(expense_file, "r") as file:
        lines = file.readlines()
    with open(expense_file, "w") as file:
        found = False
        for line in lines:
            if line.startswith(date_to_delete):
                found = True
                continue
            file.write(line)
    if found:
        print("Expense deleted successfully!")
    else:
        print("No expense found for the given date.")


def generate_report():
    """Generate a spending report by category."""
    categories = {}
    with open(expense_file, "r") as file:
        for line in file:
            _, category, amount, _ = line.strip().split(",")
            categories[category] = categories.get(category, 0) + float(amount)
    print("\nSpending Report:")
    for category, total in categories.items():
        print(f"Category: {category}, Total Spent: {total}")
    print()


def main():
    """Main menu for the Expense Tracker."""
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
