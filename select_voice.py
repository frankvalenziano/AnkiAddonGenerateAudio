from aqt.qt import QInputDialog
from aqt import mw

def select_voice_for_language(lang_choice, voices):
    voice_choice, ok = QInputDialog.getItem(
        mw, f"Select Voice for {lang_choice}",
        "Available voices:",
        voices[lang_choice],
        editable=False
    )
    if not ok:
        return None
    return voice_choice
