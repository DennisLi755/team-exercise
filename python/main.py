todo_items = []
priority = ["Routine", "Elevated", "Urgent"]
# finish all tests
# edit function items titles
# add priority
# 0 = routine, 1 = elevated, 2 = urgent
def get_todo_list():
    return todo_items

def add_item(todo_name):
    new_todo_item = {
        "title":todo_name,
        "is_completed":False,
        "priority":0
    }
    todo_items.append(new_todo_item)

    return new_todo_item

def delete_item(index):   
    if index < len(todo_items):
        todo_items.pop(index)
        return "Item Deleted"
    else:
        return "Not Found"
    
def toggle_complete_item(index):
    if index < len(todo_items):
        todo_items[index]['is_completed'] = not todo_items[index]['is_completed']
        if todo_items[index]['is_completed']:
            return "Item Completed"
        else:
            return "Item Uncompleted"
    else:
        return "Not Found"

def display_todo_list():
    print("To Do List\n__________\n")
    if len(todo_items) == 0:
        print("No Items\n")
    else:
        for index, item in enumerate(todo_items):
            if item["is_completed"]:
                print(f"{index}: [✓] {item['title']} - {priority[item['priority']]}\n")   
            else:
                print(f"{index}: [ ] {item['title']} - {priority[item['priority']]}\n") 


def display_menu(type):
    if type == "main_menu":
        print("Menu\n____\n")
        print("1. Add New Item")
        print("2. Delete Item")
        print("3. Toggle Item")
        print("4. Change Priority")
        print("5. Exit Program")
        
    pass

def get_menu_input(title, menu_range, error_message):
    user_input = input(title)
    try:
        if int(user_input) < 1 or int(user_input) > menu_range:
            print(error_message)
            return False
        else:
            return int(user_input)
    except:
        print(error_message)
        return False




def main():
    while True:
        display_todo_list()
        display_menu("main_menu")

        user_input = False
        while user_input == False:
            user_input = get_menu_input("\nSelect Menu Options: ",4,"Invalid Input")
            
        if user_input == 1:
            item_name = input("Name of item: ")
            add_item(item_name)
            pass
        elif user_input == 2:
            display_todo_list()
            item_index = int(input("Index of item to be deleted: "))
            delete_item(item_index)
            pass
        elif user_input == 3:
            item_index = int(input("Index of item to be toggled: "))
            toggle_complete_item(item_index)
            pass
        elif user_input == 4:
            item_index = int(input("Index of item to be prioritized: "))

            item_priority = get_menu_input("New Priority Level")

            toggle_complete_item(item_index)
            pass
        elif user_input == 5:
            print('Exiting Program')
            break





if __name__ == '__main__':
    main()
