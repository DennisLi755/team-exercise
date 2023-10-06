from main import add_item, delete_item, toggle_complete_item, display_todo_list, display_menu, change_priority, edit_item
import pytest

#region Unit Tests

def test_display_todo_list_empty(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\nNo Items\n\n"

def test_add_item():
    assert add_item("Vacuum") == {"title": "Vacuum", "is_completed": False, "priority": 0}

def test_display_todo_list_item(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\n0: [ ] Vacuum - Routine\n\n"

def test_toggle_complete_item():
    assert toggle_complete_item(0) == "Item Completed"

def test_toggle_complete_item_not_found():
    assert toggle_complete_item(1) == "Not Found"

def test_display_todo_list_item_completed(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\n0: [✓] Vacuum - Routine\n\n"

def test_change_priority():
    assert change_priority(0, 2) == "Priority Changed"

def test_change_priority_invalid_index():
    assert change_priority(2, 1) == "Not Found"

def test_display_todo_list_item_priority(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\n0: [✓] Vacuum - Urgent\n\n"

def test_edit_item():
    assert edit_item(0, "Shopping") == "Item Title Changed"

def test_edit_item_invalid_index():
    assert edit_item(2, "Shopping") == "Not Found"

def test_display_todo_list_edited_item(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\n0: [✓] Shopping - Urgent\n\n"

def test_delete_item_deleted():
    assert delete_item(0) == "Item Deleted"

def test_delete_item_not_found():
    assert delete_item(0) == "Not Found"

def test_display_menu(capsys):
    display_menu("main_menu")
    captured = capsys.readouterr()
    assert captured.out == "Menu\n____\n\n0. Exit Program\n1. Add New Item\n2. Edit Item\n3. Delete Item\n4. Toggle Item\n5. Change Priority\n"

#endregion