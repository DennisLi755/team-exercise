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

def main():
    print(get_todo_list())
    print(add_item("First Item"))
    print(get_todo_list())
    print(delete_item(0))
    print(get_todo_list())
    print(add_item("First Item 2.0"))
    print(add_item("Second Item 2.0"))
    print(add_item("First Item 2.0"))
    print(add_item("First Item 2.0"))
    print(get_todo_list())
    print(toggle_complete_item(0))
    print(get_todo_list())


    pass

main()
