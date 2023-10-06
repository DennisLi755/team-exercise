todo_items = []

def get_todo_list():
    return todo_items

def add_item(todo_name):
    new_todo_item = {
        "title":todo_name,
        "is_completed":False
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
        for item in todo_items:
            if item["is_completed"]:
                print(f"[✓] {item['title']}\n")   
            else:
                print(f"[ ] {item['title']}\n") 

def display_menu(type):
    if type == "Main Menu":
        print("1. Add New Item")
        print("2. Delete Item")
        print("3. Toggle Item")
        
    pass



def main():
    while True:
        display_todo_list()
        display_menu()
    

main()
