# __init__.py

# This file serves as the entry point for the Anki add-on that generates audio for note fields
# using macOS's built-in 'say' command and ffmpeg for conversion.

import os
from aqt import mw
from aqt.qt import QAction, qconnect
from aqt.utils import showInfo
from anki.notes import Note

# Importing helper utilities and modules
from .voice_registry import get_installed_voices
from .audio_utils import normalize_term, get_output_paths, synthesize_audio, convert_to_mp3
from .locale_map import get_display_name, get_locale_map
from .audio_generation_mode import get_generation_mode
from .select_language import select_language
from .select_voice import select_voice_for_language
from .note_updates import process_notes
from .select_deck import select_decks

def generate_audio_for_note(note: Note, voice: str, replace_existing=False):
    """Generate audio for a single Anki note's 'term' field using the specified voice."""
    term = note["term"].strip() if "term" in note else ""
    term = normalize_term(term)

    if not term:
        showInfo("⚠️ Skipped a note because the 'term' field was empty.")
        return

    media_dir = mw.col.media.dir()
    temp_aiff_path, media_path, filename = get_output_paths(term, media_dir)

    if os.path.exists(media_path) and not replace_existing:
        return

    try:
        synthesize_audio(term, voice, temp_aiff_path)
        convert_to_mp3(temp_aiff_path, media_path)
    except Exception as e:
        showInfo(f"❌ Error generating audio for '{term}': {e}")
    finally:
        if os.path.exists(temp_aiff_path):
            os.remove(temp_aiff_path)

    note["Audio"] = f"[sound:{filename}]"
    note.flush()

def run_audio_generation():
    """Initiate the audio generation process by walking the user through options."""
    selected_decks = select_decks()
    if not selected_decks:
        return

    voices = get_installed_voices()
    if not voices:
        showInfo("❌ Could not retrieve voices from macOS.")
        return

    replace = get_generation_mode()
    if replace is None:
        return

    locale_map = get_locale_map()
    lang_choice = select_language(voices, locale_map)
    if not lang_choice:
        return

    voice_choice = select_voice_for_language(lang_choice, voices)
    if not voice_choice:
        return

    process_notes(voice_choice, replace, generate_audio_for_note, selected_decks)

# Register a menu item in Anki's Tools menu
action = QAction("🔊 Generate Audio for Notes", mw)
qconnect(action.triggered, run_audio_generation)
mw.form.menuTools.addAction(action)
