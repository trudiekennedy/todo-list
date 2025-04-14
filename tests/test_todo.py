from lib.todo import Todo

"""
Given a task, to-do status is initially set to false
"""
def test_initial_todo_status_is_false():
    todo = Todo("Walk the dog")
    assert todo.task == "Walk the dog"
    assert todo.status == False

"""
Given a task, when user calls mark_complete, the task status is set to True
"""

def test_mark_complete_sets_status_to_true():
    todo = Todo("Walk the dog")
    todo.mark_complete()
    assert todo.status == True 