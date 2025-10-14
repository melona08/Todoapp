from journal import *
from todo import *

# =======================
# Main Program
# =======================

def main():
    todolist = load_todo()
    journal = load_journal()

    while True:
        print('\n==== TODO JOURNAL APP ====')
        print("1. Add todo")
        print("2. Remove todo")
        print("3. Edit todo")
        print("4. Show todo")
        print("5. Add journal")
        print("6. Remove journal")
        print("7. Edit journal")
        print("8. Show journal")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            todo = input("Enter your todo: ").strip()
            add_todo(todo, todolist)

        elif choice == "2":
            todo = input("Todo to remove: ").strip()
            remove_todo(todo, todolist)

        elif choice == "3":
            todo = input("Todo to edit: ").strip()
            if todo in todolist:
                newtodo = input("New todo: ").strip()
                edit_todo(todo, todolist, newtodo)
            else:
                print("Todo not found.")

        elif choice == "4":
            show_todo(todolist)

        elif choice == "5":
            title = input("Enter journal title: ").strip()
            content = input("Enter journal content: ").strip()
            add_journal(title, content, journal)

        elif choice == "6":
            title = input("Journal title to remove: ").strip()
            remove_journal(title, journal)

        elif choice == "7":
            title = input("Journal title to edit: ").strip()
            if title in journal:
                new_content = input("New journal content: ").strip()
                edit_journal(title, journal, new_content)
            else:
                print("Journal entry not found.")

        elif choice == "8":
            show_journal(journal)

        elif choice == "9":
            print("Exiting program... (everything is saved automatically)")
            break

        else:
            print("Invalid input. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
