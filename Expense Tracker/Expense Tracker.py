import csv
from datetime import datetime

FILENAME = "expenses.csv"

def load_expenses():
    try:
        with open(FILENAME, mode='r', newline='') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def add_expense():
    date = input("📅 Enter date (YYYY-MM-DD): ")
    category = input("📂 Enter category (e.g., Food, Rent, etc.): ")
    amount = input("💵 Enter amount: ")
    description = input("📝 Enter description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return
    print("\n📋 All Expenses:")
    print("Date        | Category   | Amount   | Description")
    print("-" * 50)
    for e in expenses:
        print(f"{e['date']} | {e['category']:<10} | ${e['amount']:<7} | {e['description']}")

def total_expenses():
    expenses = load_expenses()
    total = sum(float(e['amount']) for e in expenses)
    print(f"\n💰 Total Expenses: ${total:.2f}")

def filter_by_category():
    cat = input("🔍 Enter category to filter by: ")
    expenses = load_expenses()
    filtered = [e for e in expenses if e['category'].lower() == cat.lower()]
    if not filtered:
        print(f"⚠️ No expenses found in category '{cat}'.")
        return
    print(f"\n📂 Expenses in category: {cat}")
    print("Date        | Amount   | Description")
    print("-" * 40)
    for e in filtered:
        print(f"{e['date']} | ${e['amount']:<7} | {e['description']}")

def menu():
    while True:
        print("\n📒 Expense Tracker Menu")
        print("1. ➕ Add Expense")
        print("2. 📄 View All Expenses")
        print("3. 💰 Total Expenses")
        print("4. 🔎 Filter by Category")
        print("5. ❌ Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

menu()
