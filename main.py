todo_list = []
item = str
loop_variable = 0

# function to reset the loop variable
def reset_loop():
    global loop_variable
    loop_variable = 0

# function to add an item to the list
def add_item():
    item = input("\nEnter an item: ")
    todo_list.append({"Item": item, "Status": "Not Done"})
    reset_loop()

# function to change the status of an item to "Done"
def complete_item():
    # list all items in the list
    list_items()
    item_number = int(input("\nEnter the number of the item you want to complete: ")) - 1
    if 0 <= item_number < len(todo_list):
        todo_list[item_number]["Status"] = "Done"
        print("Item marked as done.")
    else:
        print("Invalid item number.")
    reset_loop()

# function to delete an item from the list
def delete_item():
    # list all items in the list
    list_items()
    item_number = int(input("\nEnter the number of the item you want to delete: ")) - 1
    if 0 <= item_number < len(todo_list):
        del todo_list[item_number]
        print("Item deleted.")
    else:
        print("Invalid item number.")
    reset_loop()

# function to list all items in the list
def list_items():
    print("\nItems:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item['Item']} - {item['Status']}")
    reset_loop()

# main loop
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
