import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(FILE_NAME, index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Bills, etc.): ").capitalize()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df, pd.DataFrame([[date, category, amount, description]],
                                     columns=df.columns)], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print(" Expense added successfully!")

def view_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print(df)

def delete_expense():
    view_expenses()
    idx = int(input("Enter row number to delete: "))
    df = pd.read_csv(FILE_NAME)
    if 0 <= idx < len(df):
        df.drop(idx, inplace=True)
        df.to_csv(FILE_NAME, index=False)
        print(" Expense deleted!")
    else:
        print(" Invalid index.")

def summary_by_category():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses to summarize.")
        return
    summary = df.groupby("Category")["Amount"].sum()
    print("\n--- Expense Summary by Category ---")
    print(summary)
    summary.plot(kind="bar", title="Expenses by Category", color="skyblue")
    plt.ylabel("Amount")
    plt.show()

def monthly_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses to summarize.")
        return
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    summary = df.groupby("Month")["Amount"].sum()
    print("\n--- Monthly Expense Summary ---")
    print(summary)
    summary.plot(kind="line", marker='o', title="Monthly Expenses", color="green")
    plt.ylabel("Amount")
    plt.show()

def main():
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summary by Category")
        print("5. Monthly Summary")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            summary_by_category()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    main()
