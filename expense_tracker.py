import argparse
import json
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(description, amount):
    expenses = load_expenses()

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    new_id = 1

    if expenses:
        new_id = max(expense["id"] for expense in expenses) + 1

    expense = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print(f"Expense added successfully (ID: {new_id})")


def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':<5}{'Date':<12}{'Description':<25}{'Amount':>10}")
    print("-" * 52)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<12}"
            f"{expense['description']:<25}"
            f"${expense['amount']:>9.2f}"
        )


def update_expense(expense_id, description, amount):
    expenses = load_expenses()

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expense["description"] = description
            expense["amount"] = amount
            save_expenses(expenses)

            print(f"Expense updated successfully (ID: {expense_id})")
            return

    print("Expense ID not found.")


def delete_expense(expense_id):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            print("Expense deleted successfully")
            return

    print("Expense ID not found.")


def summary_expenses():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total expenses: ${total:.2f}")


def summary_month(month):
    expenses = load_expenses()

    if month < 1 or month > 12:
        print("Invalid month. Please enter a month between 1 and 12.")
        return

    total = 0

    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")

        if (
            expense_date.year == datetime.now().year
            and expense_date.month == month
        ):
            total += expense["amount"]

    month_name = datetime(2000, month, 1).strftime("%B")

    print(f"Total expenses for {month_name}: ${total:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")

    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True, type=float)

    # List command
    subparsers.add_parser("list")

    # Update command
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", required=True, type=int)
    update_parser.add_argument("--description", required=True)
    update_parser.add_argument("--amount", required=True, type=float)

    # Delete command
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True, type=int)

    # Summary command
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)

    elif args.command == "list":
        list_expenses()

    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)

    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == "summary":
        if args.month:
            summary_month(args.month)
        else:
            summary_expenses()


if __name__ == "__main__":
    main()