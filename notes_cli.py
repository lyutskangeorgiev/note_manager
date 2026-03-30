import typer
import notes_logic

app = typer.Typer()
@app.command()
def add(title: str, content: str):
    """Creates a new note with a TITLE and CONTENT."""
    notes_logic.add_notes(title, content)
    typer.echo(f"{title} added in notes")

#changing the name from list_notes to list because list is a python keyword
@app.command(name="list")
def list_notes():
    """Shows a list of all saved notes."""
    notes = notes_logic.list_notes()
    if not notes:
        typer.echo("No notes saved, try adding one with add function")
        return

    last_id = notes[-1]['id']
    #we cast the biggest/last id to str and check its length
    #to calc the max width of 'the id column'
    width = len(str(last_id))
    # ':' starts formatting, '<' left-aligns, '{width}' sets dynamic spacing
    typer.echo(f"{"ID":<{width}} Title")
    # ':' starts formatting, '<' left-aligns, '{width}' sets dynamic spacing
    for note in notes:
        typer.echo(f"{note['id']:<{width}}: {note['title']}")

@app.command()
def show(note_id: int):
    """Shows the full content of a specific note by its ID."""
    try:
        note = notes_logic.get_note(note_id)
        header = f"ID: {note_id} | Title: {note['title']}"
        typer.echo(header)
        #we create line separation the size of the header for better formatting
        typer.echo("-" * len(header))
        typer.echo(note['content'])
    except ValueError as e:
        #send error to stderr so it doesn't mix with stdout if redirected (to a file for example)
        typer.echo(f"Error: {e}", err=True)

@app.command()
def delete(note_id: int):
    """Deletes a specific note by its ID."""
    try:
        notes_logic.delete_note(note_id)
        typer.echo(f"Note with ID: {note_id} deleted successfully")
    except ValueError as e:
        #send error to stderr so it doesn't mix with stdout if redirected (to a file for example)
        typer.echo(f"Error: {e}", err=True)