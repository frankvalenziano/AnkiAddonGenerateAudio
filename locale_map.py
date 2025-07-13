# locale_map.py

def locale_to_voice(note):
    lang_map = {
        "en_us": "Samantha",
        "es_es": "Mónica",
        "es_mx": "Paulina",
        "fi_fi": "Satu",
        "fr_ca": "Amélie",
        "fr_fr": "Thomas",
        "it_it": "Alice",
        "ja_jp": "Kyoko",
        "ko_kr": "Yuna",
        "pt_br": "Luciana",
        "zh_cn": "Ting-Ting",
        "zh_tw": "Meijia",
        "zh_hk": "Sinji",
        "ro_ro": "Ioana",
        "pt_pt": "Joana",
        "hr_hr": "Lana",
        "sk_sk": "Laura",
        "hi_in": "Lekha",
        "uk_ua": "Lesya",
        "vi_vn": "Linh",
        "ar_001": "Majed",
        "hu_hu": "Tünde",
        "el_gr": "Melina",
        "ru_ru": "Milena",
        "en_ie": "Moira",
        "ca_es": "Montse",
        "nb_no": "Nora",
        "de_de": "Anna",
        "en_gb": "Daniel",
        "en_au": "Karen",
        "da_dk": "Sara",
        "sl_si": "Tina",
        "ta_in": "Vani",
        "tr_tr": "Yelda",
        "nl_nl": "Xander",
        "pl_pl": "Zosia",
        "cs_cz": "Zuzana",
        "th_th": "Kanya",
        "en_za": "Tessa",
        "en_in": "Rishi",
        "zh_hant": "Sinji",  # Fallback alias for Traditional Chinese (HK)
        "zh_hans": "Ting-Ting",  # Fallback alias for Simplified Chinese
        "bg_bg": "Dariya",
        "he_il": "Carmit",
        "id_id": "Damayanti",
        "ms_my": "Laila",
        "sv_se": "Alva",
        "nl_be": "Xander",  # fallback to Dutch (Netherlands)
    }

    lang = note.get("Language", "").strip().lower().replace("-", "_")
    return lang_map.get(lang, "Samantha")  # fallback to English


LANGUAGE_LABELS = {
    "en": "English",
    "es": "Spanish",
    "fi": "Finnish",
    "fr": "French",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "pt": "Portuguese",
    "zh": "Chinese",
    "ro": "Romanian",
    "hr": "Croatian",
    "sk": "Slovak",
    "hi": "Hindi",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "ar": "Arabic",
    "hu": "Hungarian",
    "el": "Greek",
    "ru": "Russian",
    "ca": "Catalan",
    "nb": "Norwegian",
    "de": "German",
    "da": "Danish",
    "sl": "Slovenian",
    "ta": "Tamil",
    "tr": "Turkish",
    "nl": "Dutch",
    "pl": "Polish",
    "cs": "Czech",
    "th": "Thai",
    "bg": "Bulgarian",
    "he": "Hebrew",
    "id": "Indonesian",
    "ms": "Malay",
    "sv": "Swedish",
} 


def get_display_name(locale: str) -> str:
    lang_code = locale.split("_")[0]
    lang_label = LANGUAGE_LABELS.get(lang_code, lang_code.upper())
    return f"{lang_label} ({locale})"


def get_locale_map():
    return {key: key for key in LANGUAGE_LABELS}
