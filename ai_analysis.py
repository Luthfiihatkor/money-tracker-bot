def auto_category(text):

    text = text.lower()

    if "makan" in text or "food" in text:
        return "food"

    if "bensin" in text or "transport" in text:
        return "transport"

    if "game" in text or "steam" in text:
        return "entertainment"

    if "gaji" in text:
        return "income"

    return "other"
