import subprocess
import re
from collections import defaultdict

def get_installed_voices():
    """
    Parse the output of 'say -v ?' to build a dictionary mapping both full locale codes
    and base language codes to a list of voice names. More robust against spacing inconsistencies.
    """
    voices_by_locale = defaultdict(list)
    voices_by_lang = defaultdict(list)

    try:
        result = subprocess.run(['say', '-v', '?'], stdout=subprocess.PIPE, check=True)
        output = result.stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        return {}

    for line in output.strip().splitlines():
        # Looser match to handle optional whitespace and allow variations
        match = re.match(r'^(.+?)\s+([a-zA-Z_]+)\s+[#]', line)
        if not match:
            continue

        voice_name, locale = match.groups()
        locale_key = locale.strip().lower().replace("-", "_")
        lang_code = locale_key.split("_")[0]
        cleaned_name = re.sub(r'\s*\([^)]*\)', '', voice_name).strip()

        # Add to both locale and base language mappings
        if cleaned_name not in voices_by_locale[locale_key]:
            voices_by_locale[locale_key].append(cleaned_name)
        if cleaned_name not in voices_by_lang[lang_code]:
            voices_by_lang[lang_code].append(cleaned_name)

    # Merge both dictionaries, locale taking precedence
    combined = dict(voices_by_lang)
    combined.update(voices_by_locale)

    return combined
