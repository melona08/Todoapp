# add, remove, edit,  save 
# show


def add_todo(todo, todolist):
    if todo in todolist:
        print(f"'{todo} is already in todolist'")
    else:
        print(f"'{todo} is add'")
        
def remove_todo(todo, todolist):
    if todo in todolist:
        del todolist[todo]
        print(f"'{todo}is remove'")
    else:
        print('todo not found')



def edit_todo(todo, todolist, newtodo):
    if todo in todolist:
        todolist[todo] = newtodo
        print(f"'{todo}' has been updated to '{newtodo}'.")
    else:
        print("todo is not found")
        



def save_todo(todolist, filename="todo.json"):
    with open(filename, "w", encoding="utf-8") as f:
        for todo in todolist:
            f.write(f"{todo}\n")
    print("todo is saved")



def show_todo(todolist):
    if not todolist:
        print('Todolist is empty.')
    else:
        print("\n--- Current todolist ---")
        for i, (todo) in enumerate(todolist, 1):
            print(f"{i}. {todo}")
