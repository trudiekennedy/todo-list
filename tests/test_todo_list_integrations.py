from lib.todo import *
from lib.todo_list import *

"""
When a to-do is added which have not been completed
The to-do list has one task stored with status as False
"""
def test_a_single_todo_is_stored_to_list():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todos.add(todo_1)
    assert todos._my_list == [todo_1]


"""
When two to-dos are added which have not been completed
The to-do list has two tasks stored with status as False
"""

def test_two_todos_are_stored_to_list():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    print(todos._my_list)
    assert todos._my_list == [todo_1, todo_2]
"""
When two to-dos are added which have not been completed
And the user calls for the incomplete to-dos
The return to-do list will have the details of the two tasks (without the status)

"""
def test_find_incomplete_tasks():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    assert todos.incomplete() == ["Walk the dog", "Clean the dishes"]

"""
When two to-dos are added and one has been completed
And the user calls for the incomplete to-dos
The return to-do list will have the details of one incomplete task (without the status)

"""
def test_find_incomplete_tasks_where_one_is_completed():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    todo_1.mark_complete()
    assert todos.incomplete() == ["Clean the dishes"]

"""
When two to-dos are added and both have been completed
And the user calls for the incomplete to-dos
The return to-do list will return an empty list

"""
def test_find_incomplete_tasks_where_both_completed():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todos.incomplete() == []

"""
When two to-dos are added and one has been completed
And the user calls for the complete to-dos
The return to-do list will have the details of one complete task (without the status)

"""
def test_find_complete_tasks_where_one_is_completed():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    todo_1.mark_complete()
    assert todos.complete() == ["Walk the dog"]

"""
When two to-dos are added and both have been completed
And the user calls for the complete to-dos
The return to-do list will have the details both complete tasks (without the status)

"""
def test_find_complete_tasks_where_both_completed():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todos.complete() == ["Walk the dog", "Clean the dishes"]

"""
When two to-dos are added and both are incomplete
And the user calls for the complete to-dos
The return to-do list will return an empty list

"""
def test_find_complete_tasks_where_both_incomplete():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    assert todos.complete() == []

"""
When two to-dos are added and both are incomplete
And the user calls #give_up
All of the to-dos in todo list are marked as True
And when the user calls #complete, both to-dos are returned

"""
def test_all_tests_complete_when_user_gives_up():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    todos.give_up()
    assert todos.complete() == ["Walk the dog", "Clean the dishes"]

"""
When two to-dos are added and both are incomplete
And the user calls #give_up
All of the to-dos in todo list are marked as True
And when the user calls #incomplete, an empty list is returned

"""
def test_all_tests_complete_when_user_gives_up_nothing_is_incomplete():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    todos.give_up()
    assert todos.incomplete() == []

"""
When two to-dos are added and one is marked complete 
And the user calls #give_up
All of the to-dos in todo list are marked as True
And when the user calls #complete, both tasks are returned

"""
def test_all_tests_complete_when_user_gives_up_halfway():
    todos = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Clean the dishes")
    todos.add(todo_1)
    todos.add(todo_2)
    todo_1.mark_complete()
    todos.give_up()
    assert todos.complete() == ["Walk the dog", "Clean the dishes"]