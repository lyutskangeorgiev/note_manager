# Note Manager

A simple, user-friendly command-line note-taking application built with Python.

## Installation & Setup

To run this project locally, follow these steps:

1. Ensure you have Python 3 installed.
2. Clone the repository:
   `git clone <your-github-repo-link>`
3. Install the required dependencies from `requirements.txt`:
   `pip install -r requirements.txt`

## Usage & Commands

The application is run via `main.py` and supports the following commands:

* **Add a new note:**
  `python main.py add "Title" "Content"`
  - *Description: Creates a new note with the specified title and content.*

* **List all notes:**
  `python main.py list`
  - *Description: Lists all notes that are currently saved in the file, if there aren't any it returns an instructional message.*

* **Show a specific note:**
  `python main.py show 1`
  - *Description: Prints the note with the specified ID, if a note with that ID doesn't exist it prints an error message.*

* **Delete a note:**
  `python main.py delete 1`
  - *Description: Deletes the note with the specified ID, if a note with that ID doesn't exist it prints an error message.*

## Testing

This project uses `pytest` for automated testing. 

To run the tests, execute the following command in your terminal: `pytest`