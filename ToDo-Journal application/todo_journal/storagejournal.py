# add, remove, edit,  save 
# show


def add_journal(diary, journal):
    if diary in journal:
        print(f"'{diary}' already in the journal.")
    else:
        print(f"'{diary}' has been added.")
        

def remove_journal(diary, journal):
    if diary in journal:
        del journal[diary]
        print(f"'{diary}' is removed.")
    else:
        print("song not found.")
        
        
def edit_journal(diary, journal, newdiary):
    if diary in journal:
        journal[diary] = newdiary
        print(f"'{diary}' has been updated to '{newdiary}'")
    else:
        print("diary not found")
        
        
def save_journal(journal, filename="journal.json"):
    with open(filename, "w", encoding="utf-8") as f:
        for diary in journal:
            f.write(f"'{diary}'\n")
    print("Journal has been saved.")
    
    
def show_journal(journal):
    if not journal:
        print("journal is empty.")
    else:
        print('\n--- Current journal ---')    
        for i, (diary) in enumerate(journal, i):
            print(f"{i}. {diary}")
    