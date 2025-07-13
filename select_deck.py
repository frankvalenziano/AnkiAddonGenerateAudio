from aqt import mw
from aqt.qt import QInputDialog

def select_deck():
    """
    Prompts the user to choose a single deck from all available decks in the collection.
    Returns the selected deck name or None if canceled.
    """
    deck_names = list(mw.col.decks.all_names())
    deck_names.sort()

    deck, ok = QInputDialog.getItem(
        mw, "Select Deck",
        "Choose a deck to process:",
        deck_names,
        editable=False
    )
    return deck if ok else None

def is_note_in_selected_deck(note, selected_deck_name):
    """
    Checks if the given note belongs to the selected deck by examining its cards.
    Returns True if any of the note's cards belong to the selected deck.
    """
    card_ids = note.card_ids()
    for cid in card_ids:
        card = mw.col.get_card(cid)
        deck = mw.col.decks.name(card.did)
        if deck == selected_deck_name:
            return True
    return False
