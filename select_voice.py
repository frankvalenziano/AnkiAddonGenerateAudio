from aqt.qt import QInputDialog
from aqt import mw

def select_voice_for_language(lang_choice, voices):
    # Gather all voices for any locale that starts with the language code (e.g., 'it' matches 'it_it')
    matching_voices = []
    for locale_key, voice_list in voices.items():
        if locale_key.startswith(lang_choice):
            matching_voices.extend(voice_list)

    # Remove duplicates and sort
    matching_voices = sorted(set(matching_voices))

    # If no matches found, show fallback message
    if not matching_voices:
        matching_voices = ["No voices available"]

    voice_choice, ok = QInputDialog.getItem(
        mw, f"Select Voice for {lang_choice}",
        "Available voices:",
        matching_voices,
        editable=False
    )
    if not ok or voice_choice == "No voices available":
        return None
    return voice_choice
