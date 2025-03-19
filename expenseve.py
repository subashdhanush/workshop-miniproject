import csv

def add_expense(amount, category):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

def view_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense(input("Amount: "), input("Category: "))
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
