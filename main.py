import json
import os

todo_list = []
item = str
loop_variable = 0

# File to save and load the todo list
TODO_FILE = "todo_list.json"

# Function to load the todo list from the file
def load_todo_list():
    global todo_list
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            todo_list = json.load(file)
    else:
        todo_list = []

# Function to save the todo list to the file
def save_todo_list():
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file)

# Function to reset the loop variable
def reset_loop():
    global loop_variable
    loop_variable = 0

# Function to add an item to the list
def add_item():
    item = input("\nEnter an item: ")
    todo_list.append({"Item": item, "Status": "Not Done"})
    save_todo_list()
    reset_loop()

# Function to change the status of an item to "Done"
def complete_item():
    # List all items in the list
    list_items()
    item_number = int(input("\nEnter the number of the item you want to complete: ")) - 1
    if 0 <= item_number < len(todo_list):
        todo_list[item_number]["Status"] = "Done"
        save_todo_list()
        print("Item marked as done.")
    else:
        print("Invalid item number.")
    reset_loop()

# Function to delete an item from the list
def delete_item():
    # List all items in the list
    list_items()
    item_number = int(input("\nEnter the number of the item you want to delete: ")) - 1
    if 0 <= item_number < len(todo_list):
        del todo_list[item_number]
        save_todo_list()
        print("Item deleted.")
    else:
        print("Invalid item number.")
    reset_loop()

# Function to list all items in the list
def list_items():
    print("\nItems:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item['Item']} - {item['Status']}")
    reset_loop()

# Load the todo list when the program starts
load_todo_list()

# Main loop
while loop_variable == 0:
    print("\n1. Add item")
    print("2. Complete item")
    print("3. Delete item")
    print("4. List items")
    print("5. Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        complete_item()
    elif choice == 3:
        delete_item()
    elif choice == 4:
        list_items()
    elif choice == 5:
        loop_variable = 1
    else:
        print("Invalid choice. Please try again.")
        reset_loop()
