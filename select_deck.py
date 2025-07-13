from aqt import mw
from aqt.qt import QDialog, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton

def select_decks():
    """
    Opens a custom dialog allowing the user to select multiple decks.
    Returns a list of selected deck names, or None if canceled.
    """
    dialog = QDialog(mw)
    dialog.setWindowTitle("Select Decks")

    layout = QVBoxLayout()
    deck_list = QListWidget()
    deck_list.setSelectionMode(QListWidget.MultiSelection)

    for name in sorted(mw.col.decks.all_names()):
        item = QListWidgetItem(name)
        deck_list.addItem(item)

    layout.addWidget(deck_list)

    confirm_button = QPushButton("OK")
    confirm_button.clicked.connect(dialog.accept)
    layout.addWidget(confirm_button)

    dialog.setLayout(layout)

    if dialog.exec():
        return [item.text() for item in deck_list.selectedItems()]
    return None

def is_note_in_selected_decks(note, selected_deck_names):
    """
    Checks if the note belongs to any of the selected decks.
    """
    card_ids = note.card_ids()
    for cid in card_ids:
        card = mw.col.get_card(cid)
        deck = mw.col.decks.name(card.did)
        if deck in selected_deck_names:
            return True
    return False
