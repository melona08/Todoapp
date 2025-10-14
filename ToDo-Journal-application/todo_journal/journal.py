from config import *
import json
import os

# =======================
# Journal Functions (dict)
# =======================

def load_journal(filename=JOURNAL_FILE):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_journal(journal, filename=JOURNAL_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(journal, f, indent=4)

def add_journal(title, content, journal):
    if title in journal:
        print(f"'{title}' is already in the journal.")
    else:
        journal[title] = content
        save_journal(journal)
        print(f"'{title}' has been added.")

def remove_journal(title, journal):
    if title in journal:
        del journal[title]
        save_journal(journal)
        print(f"'{title}' has been removed.")
    else:
        print("Journal entry not found.")

def edit_journal(title, journal, new_content):
    if title in journal:
        journal[title] = new_content
        save_journal(journal)
        print(f"'{title}' has been updated.")
    else:
        print("Journal entry not found.")

def show_journal(journal):
    if not journal:
        print("Journal is empty.")
    else:
        print('\n--- Current Journal Entries ---')    
        for i, (title, content) in enumerate(journal.items(), 1):
            snippet = content[:40] + ('...' if len(content) > 40 else '')
            print(f"{i}. {title} — {snippet}")