from lib.todo_list import TodoList

"""
Initially, TodoList is an empty list
"""

def test_todo_list_empty_to_start():
    todos = TodoList()
    assert todos._my_list == []