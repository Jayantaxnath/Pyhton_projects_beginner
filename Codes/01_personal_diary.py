# Project_04
import json
from datetime import datetime

# File to store diary entries
FILE_NAME = "diary_entries.json"


# Load existing entries from the file
def load_entries():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save entries to the file
def save_entries(entries):
    with open(FILE_NAME, "w") as file:
        json.dump(entries, file, indent=4)


# Add a new diary entry
def add_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    content = input("Write your diary entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"date": date, "content": content, "timestamp": timestamp}

    entries = load_entries()
    entries.append(entry)
    save_entries(entries)
    print("Diary entry added successfully!")


# View diary entries
def view_entries():
    entries = load_entries()
    if not entries:
        print("No diary entries found.")
        return

    print("\nDiary Entries:")
    for i, entry in enumerate(entries, 1):
        print(f"\nEntry {i}:")
        print(f"Date: {entry['date']}")
        print(f"Time: {entry['timestamp']}")
        print(f"Content: {entry['content']}")


# Delete an entry by date
def delete_entry():
    date = input("Enter the date of the entry to delete (YYYY-MM-DD): ")
    entries = load_entries()
    updated_entries = [entry for entry in entries if entry["date"] != date]

    if len(entries) == len(updated_entries):
        print("No entry found for the given date.")
    else:
        save_entries(updated_entries)
        print("Diary entry deleted successfully!")


# Main menu
def main():
    while True:
        print("\nPersonal Diary Application")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Delete Entry")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            delete_entry()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
