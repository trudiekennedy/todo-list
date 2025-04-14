class TodoList:
    def __init__(self):
        self._my_list = []

    def add(self, todo):
        self._my_list.append(todo)

    def incomplete(self):
        still_todo = []
        for todo in self._my_list:
            if todo.status == False:
                still_todo.append(todo.task)
        return still_todo

    def complete(self):
        completed_todos = []
        for todo in self._my_list:
            if todo.status == True:
                completed_todos.append(todo.task)
        return completed_todos

    def give_up(self):
        for todo in self._my_list:
            todo.status = True