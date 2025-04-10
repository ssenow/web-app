FILEPATH = "todos.txt"
def get_todos(filepath= FILEPATH):

    """Read the text files and return todo items in a list"""
    with open(filepath,"r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos, filepath= FILEPATH):
    """write the changed todos to the file"""
    with open(filepath, "w") as file:
        file.writelines(todos)
