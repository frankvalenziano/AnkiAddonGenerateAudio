from aqt import mw
from aqt.utils import showInfo
from .select_deck import is_note_in_selected_deck

def process_notes(voice_choice, replace, generate_audio_for_note, selected_deck=None):
    mw.checkpoint("Generate Audio")
    note_ids = mw.col.db.list("SELECT id FROM notes")
    notes = [mw.col.get_note(nid) for nid in note_ids]
    updated = 0

    for note in notes:
        if selected_deck and not is_note_in_selected_deck(note, selected_deck):
            continue
        if "term" in note and ("Audio" not in note or not note["Audio"].strip() or replace):
            generate_audio_for_note(note, voice_choice, replace_existing=replace)
            updated += 1

    showInfo(f"✅ Audio generated for {updated} notes using voice: {voice_choice}")
