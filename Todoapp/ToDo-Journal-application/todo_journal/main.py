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
        print("5. complete todo: ")
        print("6. Add journal")
        print("7. Remove journal")
        print("8. Edit journal")
        print("9. Show journal")
        print("10. Exit")
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
            todo = input("Enter completed todo: ")
            completed(todo, todolist)

        elif choice == "6":
            title = input("Enter journal title: ").strip()
            content = input("Enter journal content: ").strip()
            
            emotions = input("Enter emotions: 1.😊 2.🙂 3.😐 4.🙁 5.😂 6.😲 7.😴 8.😡 9.😭 10.🤗 11.🤔")
            
            if emotions == "1":
                emotions = "😊"
            elif emotions == "2":
                emotions = "🙂"
            elif emotions =="3":
                emotions = "😐"
            elif emotions == "4":
                emotions = "🙁"
            elif emotions == "5":
                emotions = "😂"
            elif emotions == "6":
                emotions = "😲"
            elif emotions == "7":
                emotions = "😴"
            elif emotions == "8":
                emotions = "😡"
            elif emotions == "9":
                emotions = "😭"
            elif emotions == "10":
                emotions ="🤗"
            elif emotions == "11":
                emotions = "🤔"
            else:
                print("Invalid input. Please try again.")
            
            weather = input("Enter weather: 1.☀️ 2.🌤️ 3.⛅ 4.🌥️ 5.☁️ 6.🌧️ 7.⛈️ 8.❄️ 9.🌫️ 10.🌪️")
            
            if weather == "1":
                weather = "☀️"
            elif weather == "2":
                weather = "🌤️"
            elif weather =="3":
                weather = "⛅"
            elif weather == "4":
                weather = "🌥️"
            elif weather == "5":
                weather = "😂"
            elif weather == "6":
                weather = "🌧️"
            elif weather == "7":
                weather = "⛈️"
            elif weather == "8":
                weather = "❄️"
            elif weather == "9":
                weather = "🌫️"
            elif weather == "10":
                weather ="🌪️"
            else:
                print("Invalid input. Please try again.")
            
            add_journal(title, content, journal, emotions, weather)
        

        elif choice == "7":
            title = input("Journal title to remove: ").strip()
            remove_journal(title, journal)

        elif choice == "8":
            title = input("Journal title to edit: ").strip()
            if title in journal:
                new_content = input("New journal content: ").strip()
                edit_journal(title, journal, new_content)
            else:
                print("Journal entry not found.")

        elif choice == "9":
            show_journal(journal)

        elif choice == "10":
            print("Exiting program... (everything is saved automatically)")
            break

        else:
            print("Invalid input. Please try again.")
            

# Run the program
if __name__ == "__main__":
    main()
