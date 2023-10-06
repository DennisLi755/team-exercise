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

def change_priority(index, new_priority):
    if index < len(todo_items):
        todo_items[index]['priority'] = new_priority
        return "Priority Changed"
    else:
        return "Not Found"


def delete_item(index):   
    if index < len(todo_items):
        todo_items.pop(index)
        return "Item Deleted"
    else:
        return "Not Found"
    
def edit_item(index,title):   
    if index < len(todo_items):
        todo_items[index]['title'] = title
        return "Item Title Changed"
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
    elif type == "priority":
        print("Priority Type\n_______\n")
        print("0. Routine")
        print("1. Elevated")
        print("2. Urgent")
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


# def convert_input_as_number(user_input):
#     try:
#         return int(user_input)
#     except:
#         return False

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
        elif user_input == 2:
            display_todo_list()
            item_index = int(input("Index of item to be deleted: "))
            delete_item(item_index)
            # item_index = convert_input_as_number(input("Index of item to be deleted: "))
            # if item_index !== False: 
            #     delete_item(item_index)
            # else:
            #     print("Invalid Input: Try again")
            
        elif user_input == 3:
            item_index = int(input("Index of item to be toggled: "))
            toggle_complete_item(item_index)
            # item_index = convert_input_as_number(input("Index of item to be toggled: "))
            # if item_index !== False: 
            #     toggle_complete_item(item_index)
            # else:
            #     print("Invalid Input: Try again")

        elif user_input == 4:
            # item_index = convert_input_as_number(input("Index of item to be prioritized: "))
            item_index = int(input("Index of item to be prioritized: "))
            # toggle_complete_item(item_index)

            # if item_index == False: 
            #     print("Invalid Input: Try again")
            #     continue

            display_menu("priority")
            item_priority_input = False
            while item_priority_input == False:
                item_priority_input = get_menu_input("New Priority Level: ",3,"Invalid Input")

            change_priority(item_index,item_priority_input)

        elif user_input == 5:
            print('Exiting Program')
            break

if __name__ == '__main__':
    main()
