tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def view_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number!")

while True:
    choice = input("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit\nChoose: ")
    if choice == "1":
        add_task(input("Enter task: "))
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        delete_task(int(input("Enter task number to delete: ")) - 1)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
