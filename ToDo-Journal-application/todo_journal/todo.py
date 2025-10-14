from config import *
import os

# =======================
# Todo Functions (list)
# =======================

def load_todo(filename=TODO_FILE):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    return []

def save_todo(todolist, filename=TODO_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        for todo in todolist:
            f.write(f"{todo}\n")

def add_todo(todo, todolist):
    if todo in todolist:
        print(f"'{todo}' is already in the todo list.")
    else:
        todolist.append(todo)
        save_todo(todolist)
        print(f"'{todo}' has been added.")

def remove_todo(todo, todolist):
    if todo in todolist:
        todolist.remove(todo)
        save_todo(todolist)
        print(f"'{todo}' has been removed.")
    else:
        print("Todo not found.")

def edit_todo(todo, todolist, newtodo):
    if todo in todolist:
        index = todolist.index(todo)
        todolist[index] = newtodo
        save_todo(todolist)
        print(f"'{todo}' has been updated to '{newtodo}'.")
    else:
        print("Todo not found.")

def show_todo(todolist):
    if not todolist:
        print("Todo list is empty.")
    else:
        print("\n--- Current Todo List ---")
        for i, todo in enumerate(todolist, 1):
            print(f"{i}. {todo}")