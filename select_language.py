from aqt.qt import QInputDialog
from aqt import mw
from .locale_map import locale_to_voice, get_display_name

def select_language(voices, locale_map):
    # Map from base language or dialect to display label and locale
    grouped = {}
    seen_langs = set()

    for locale in sorted(voices.keys()):
        mapped_locale = locale_map.get(locale, locale).lower().replace("-", "_")
        base_lang = mapped_locale.split("_")[0]

        # Include dialects for certain languages (English, Portuguese, Chinese)
        keep_dialect = base_lang in {"en", "pt", "zh"}

        if keep_dialect:
            display_key = mapped_locale  # show en_us vs en_gb
        else:
            display_key = base_lang

        if display_key not in grouped:
            label = get_display_name(mapped_locale)
            grouped[display_key] = (label, mapped_locale)

    display_names = [label for label, _ in grouped.values()]
    display_to_locale = {label: mapped for label, mapped in grouped.values()}

    lang_choice_label, ok = QInputDialog.getItem(
        mw, "Select Language",
        "Available languages:",
        display_names,
        editable=False
    )
    if not ok:
        return None
    return display_to_locale.get(lang_choice_label, lang_choice_label)
