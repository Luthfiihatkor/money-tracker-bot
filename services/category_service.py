def detect_category(note):

    n = note.lower()

    if "makan" in n or "food" in n:
        return "food"

    if "kopi" in n:
        return "food"

    if "bensin" in n:
        return "transport"

    if "belanja" in n:
        return "shopping"

    if "internet" in n:
        return "utility"

    if "bisnis" in n:
        return "business"

    return "other"
