import csv
from datetime import datetime

expenses = []

def load_expenses(filename="expenses.csv"):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        pass

def save_expenses(filename="expenses.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "amount", "description", "category"])
        for expense in expenses:
            writer.writerow([expense["date"], expense["amount"], expense["description"], expense["category"]])

def add_expense():
    try:
        date = input("Date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")
        amount = float(input("Amount: "))
        description = input("Description: ")
        category = input("Category: ")
        expenses.append({"date": date, "amount": amount, "description": description, "category": category})
    except ValueError:
        print("Invalid input. Please try again.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(f"{expense['date']} | {expense['amount']} | {expense['description']} | {expense['category']}")

def monthly_summary():
    try:
        month = int(input("Month (1-12): "))
        year = int(input("Year: "))
        total = sum(e["amount"] for e in expenses if datetime.strptime(e["date"], "%Y-%m-%d").month == month and datetime.strptime(e["date"], "%Y-%m-%d").year == year)
        print(f"Total for {month}/{year}: ₹{total}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def category_analysis():
    category_totals = {}
    for expense in expenses:
        category_totals[expense["category"]] = category_totals.get(expense["category"], 0) + expense["amount"]
    for category, total in category_totals.items():
        print(f"{category}: ₹{total}")

def menu():
    load_expenses()
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Monthly Summary\n4. Category Analysis\n5. Save and Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            save_expenses()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
