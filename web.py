import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

#title function returns a title instace
st.title("My Todo App")
st.subheader("This is my todo app. ")
st.write("This app is designed to increase productivity.")

# provide a dynamic key to checkboxes
for index, todo in enumerate(todos):
    # stores todo value as true or false then
    checkbox = st.checkbox(todo, key=todo)
    # check if box is true or false, provide a enumerate object on todos
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

#needs a label argument
st.text_input(label="Enter a ToDO", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")