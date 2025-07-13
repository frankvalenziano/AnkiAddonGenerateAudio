import subprocess
import re
from collections import defaultdict

def get_installed_voices():
    """
    Parse the output of 'say -v ?' to build a dictionary mapping locale codes
    to a list of voice names. Handles complex cases like parenthetical names.
    """
    voices_by_locale = defaultdict(list)

    try:
        result = subprocess.run(['say', '-v', '?'], stdout=subprocess.PIPE, check=True)
        output = result.stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        return {}

    for line in output.strip().splitlines():
        # Example line:
        # "Reed (Spanish (Mexico))   es_MX    # Hola! Me llamo Reed."
        match = re.match(r'^(.+?)\s{2,}([a-zA-Z_]+)\s{2,}#', line)
        if not match:
            continue

        voice_name, locale = match.groups()
        locale_key = locale.strip().lower().replace("-", "_")
        # Strip any parenthetical info from the voice name
        cleaned_name = re.sub(r'\s*\([^)]*\)', '', voice_name).strip()

        voices_by_locale[locale_key].append(cleaned_name)

    return dict(voices_by_locale)
