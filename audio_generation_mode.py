from aqt.qt import QInputDialog
from aqt import mw

def get_generation_mode():
    mode_choice, ok = QInputDialog.getItem(
        mw, "Audio Generation",
        "Choose an option:",
        ["Generate audio only for missing entries", "Regenerate audio for all notes"],
        editable=False
    )
    if not ok:
        return None
    return mode_choice == "Regenerate audio for all notes"
