FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todo items."""
    with open(filepath) as local_file:
        todos_local = local_file.readlines()

    return todos_local

def write_todos(todos_args, filename=FILEPATH ):
    """Write the to-do items list in a text file"""
    with open(filename, 'w') as file:
        file.writelines(todos_args)
    #doesn't need a return

if __name__ == "__main__":
    print("hello")
    print(get_todos())