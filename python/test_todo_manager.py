from main import add_item, delete_item, toggle_complete_item
import pytest

def test_add_item():
    assert add_item("Vacuum") == {"title": "Vacuum", "is_completed": False}

def test_toggle_complete_item():
    assert toggle_complete_item(0) == "Item Completed"

def test_toggle_complete_item_not_found():
    assert toggle_complete_item(1) == "Not Found"

def test_delete_item_deleted():
    assert delete_item(0) == "Item Deleted"

def test_delete_item_not_found():
    assert delete_item(0) == "Not Found"