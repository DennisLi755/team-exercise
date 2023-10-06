from main import add_item, delete_item, toggle_complete_item, display_todo_list, display_menu
import pytest

#region Unit Tests

def test_display_todo_list_empty(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\nNo Items\n\n"

def test_add_item():
    assert add_item("Vacuum") == {"title": "Vacuum", "is_completed": False}

def test_display_todo_list_item(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\n0: [ ] Vacuum\n\n"

def test_toggle_complete_item():
    assert toggle_complete_item(0) == "Item Completed"

def test_toggle_complete_item_not_found():
    assert toggle_complete_item(1) == "Not Found"

def test_display_todo_list_item_completed(capsys):
    display_todo_list()
    captured = capsys.readouterr()
    assert captured.out == "To Do List\n__________\n\n0: [✓] Vacuum\n\n"

def test_delete_item_deleted():
    assert delete_item(0) == "Item Deleted"

def test_delete_item_not_found():
    assert delete_item(0) == "Not Found"

def test_display_menu(capsys):
    display_menu("main_menu")
    captured = capsys.readouterr()
    assert captured.out == "Menu\n____\n\n1. Add New Item\n2. Delete Item\n3. Toggle Item\n4. Exit Program\n"

#endregion