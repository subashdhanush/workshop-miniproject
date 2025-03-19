contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    with open("contacts.txt", "a") as file:
        file.write(f"{name}: {phone}\n")
    print(f"Contact {name} saved.")

def view_contacts():
    with open("contacts.txt", "r") as file:
        print(file.read())

while True:
    choice = input("1. Add Contact\n2. View Contacts\n3. Exit\nChoose: ")
    if choice == "1":
        add_contact(input("Name: "), input("Phone: "))
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
