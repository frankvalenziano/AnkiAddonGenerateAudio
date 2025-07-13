from aqt.qt import QInputDialog
from aqt import mw
from .locale_map import locale_to_voice, get_display_name

def select_language(voices, locale_map):
    # locale_map is now passed as an argument
    display_names = []
    display_to_locale = {}
    for locale in sorted(voices.keys()):
        mapped_locale = locale_map.get(locale, locale)
        label = get_display_name(mapped_locale)
        display_names.append(label)
        display_to_locale[label] = mapped_locale

    lang_choice_label, ok = QInputDialog.getItem(
        mw, "Select Language",
        "Available languages:",
        display_names,
        editable=False
    )
    if not ok:
        return None
    return display_to_locale.get(lang_choice_label, lang_choice_label)
