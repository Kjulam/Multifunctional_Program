def string_to_unicode(text):
    result = ""
    for char in text:
        unicode_str = f"\\u{hex(ord(char))[2:].zfill(4).upper()}"
        result += unicode_str
    return result
