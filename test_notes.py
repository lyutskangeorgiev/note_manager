import pytest
import notes_logic

@pytest.fixture(autouse=True)
def mock_notes_file (monkeypatch, tmp_path):
    """Redirect NOTES_FILE to a temporary path to isolate the test"""
    mock_file = tmp_path / "test_notes.json"
    monkeypatch.setattr(notes_logic, "NOTES_FILE", str(mock_file))

def test_add_and_list_notes():
    notes_logic.add_notes("Test Title", "Test Content")
    notes = notes_logic.list_notes()
    assert len(notes) == 1
    assert notes[0]["id"] == 1
    assert notes[0]["title"] == "Test Title"
    assert notes[0]["content"] == "Test Content"

def test_delete_note():
    notes_logic.add_notes("Test Title", "Test Content")
    id = notes_logic.list_notes()[0]["id"]
    notes_logic.delete_note(id)
    notes = notes_logic.list_notes()
    assert notes == []

def test_invalid_id_raises_error():
    with pytest.raises(ValueError):
        notes_logic.delete_note(999)
