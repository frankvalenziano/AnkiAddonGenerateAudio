import os
import re
import subprocess
import tempfile
from aqt import mw
from aqt.qt import QAction, qconnect
from aqt.utils import showInfo
from anki.notes import Note

def generate_audio_for_note(note: Note, replace_existing=False):
    import time
    term = note["term"].strip() if "term" in note else ""
    term = term.replace('\u00A0', ' ').replace('\xa0', ' ').replace('&nbsp;', ' ')  # Normalize all nbsp variants
    if not term:
        showInfo("⚠️ Skipped a note because the 'term' field was empty.")
        return

    sanitized_term = re.sub(r"[^\w\-]", "_", term)
    filename = f"{sanitized_term}.mp3"
    media_dir = mw.col.media.dir()
    media_path = os.path.join(media_dir, filename)
    temp_aiff_path = os.path.join(media_dir, f"{sanitized_term}_{int(time.time())}.aiff")

    if os.path.exists(media_path) and not replace_existing:
        return

    try:
        print(f"🔊 Using say command for: {term}")
        subprocess.run([
            'say',
            '-v', 'Alice',
            '-o', temp_aiff_path,
            term
        ], check=True)

        print(f"🎧 Converting to mp3 with ffmpeg")
        subprocess.run([
            '/opt/homebrew/bin/ffmpeg',
            '-y',
            '-i', temp_aiff_path,
            '-codec:a', 'libmp3lame',
            '-qscale:a', '2',
            media_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        showInfo(f"❌ Error generating audio for '{term}': {e}")
    finally:
        if os.path.exists(temp_aiff_path):
            os.remove(temp_aiff_path)

    note["Audio"] = f"[sound:{filename}]"
    note.flush()

def run_audio_generation():
    from aqt.utils import askUser
    from aqt.qt import QMessageBox
    replace = askUser("Do you want to replace existing audio files?", defaultno=True)

    mw.checkpoint("Generate Audio")
    note_ids = mw.col.db.list("SELECT id FROM notes")
    notes = [mw.col.get_note(nid) for nid in note_ids]
    updated = 0

    for note in notes:
        if "term" in note and ("Audio" not in note or not note["Audio"].strip() or replace):
            generate_audio_for_note(note, replace_existing=replace)
            updated += 1

    showInfo(f"✅ Audio generated for {updated} notes.")

action = QAction("🔊 Generate Missing Audio for Notes", mw)
qconnect(action.triggered, run_audio_generation)
mw.form.menuTools.addAction(action)
