import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    """Reads notes from the JSON file and returns them as a list of dictionaries."""
    # Prevent FileNotFoundError on first run by returning an empty list as default
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as f:
        notes = json.load(f)
        return notes

def save_notes(notes):
    """Saves the list of notes to the JSON file."""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)
    return

def add_notes(title, content):
    """Adds notes to the JSON file."""
    notes = load_notes()
    if not notes:
        new_id = 1
    # Take ID of last element and add 1 o have auto-incrementing ID
    else:
        new_id = notes[-1]['id'] + 1
    notes.append({'id': new_id, 'title': title, 'content': content})
    save_notes(notes)

def list_notes():
    """Returns all notes."""
    return load_notes()

def get_note(note_id):
    """Gets a note from the JSON file."""
    notes = load_notes()
    note = None
    for item in notes:
        if item['id'] == note_id:
            note = item
            break
    if not note:
        raise ValueError(f"Note with ID {note_id} not found.")
    return note

def delete_note(note_id):
    """Deletes a note from the JSON file."""
    notes = load_notes()
    for i, note in enumerate(notes):
        if note['id'] == note_id:
            del notes[i]
            save_notes(notes)
            return

    raise ValueError(f"Note with ID {note_id} not found.")