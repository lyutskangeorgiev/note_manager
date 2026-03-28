import json
import os

# File name where data will live
NOTES_FILE = "notes.json"

def load_notes():
    """Reads notes from the JSON file and returns them as a list of dictionaries."""
    #check if the file exist
    if not os.path.exists(NOTES_FILE):
        return []
    #load json in the list of dicts
    with open(NOTES_FILE, 'r') as f:
        notes = json.load(f)
        return notes

def save_notes(notes):
    """Saves the list of notes to the JSON file."""
    #dump the list of dicts (notes) in the json with format
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)
    return

def add_notes(title, content):
    """Adds notes to the JSON file."""
    notes = load_notes()
    if not notes:
        new_id = 1
    else:
        new_id = notes[-1]['id'] + 1
    notes.append({'id': new_id, 'title': title, 'content': content})
    save_notes(notes)