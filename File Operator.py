import os
from datetime import datetime


class JournalManager:

    def add_entry(self):
        entry = input("Enter your journal entry: ")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            file = open("journal.txt", "x")
            file.write(time + " - " + entry + "\n")
            file.close()

        except FileExistsError:
            file = open("journal.txt", "a")
            file.write(time + " - " + entry + "\n")
            file.close()

        print("Entry added successfully")


    def view_entries(self):
        try:
            file = open("journal.txt", "r")
            data = file.read()
            file.close()

            print("\n--- Journal Entries ---")
            print(data)

        except FileNotFoundError:
            print("No journal found")


    def search_entry(self):
        word = input("Enter keyword or date to search: ")

        try:
            file = open("journal.txt", "r")

            found = False

            for line in file:
                if word.lower() in line.lower():
                    print(line, end="")
                    found = True

            file.close()

            if not found:
                print("No matching entry found")

        except FileNotFoundError:
            print("No journal found")


    def delete_entries(self):
        if not os.path.exists("journal.txt"):
            print("No journal found")
            return

        confirm = input("Delete all entries? (yes/no): ")

        if confirm.lower() == "yes":

            try:
                file = open("journal.txt", "w")
                file.close()

                os.remove("journal.txt")

                print("All entries deleted")

            except PermissionError:
                print("Permission denied")

        else:
            print("Delete cancelled")


journal = JournalManager()


while True:

    print()
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        journal.add_entry()

    elif choice == 2:
        journal.view_entries()

    elif choice == 3:
        journal.search_entry()

    elif choice == 4:
        journal.delete_entries()

    elif choice == 5:
        print("Thank you for using Journal Manager")
        break

    else:
        print("Invalid choice")