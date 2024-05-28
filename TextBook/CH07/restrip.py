def custom_strip(string, chars=None):
    if chars is None:
        return string.strip()
    else:
        return string.strip(chars)

text = "   Hello, okinawa!   "
print(custom_strip(text))

text_with_chars = "---Hello, okinawa!---"
print(custom_strip(text_with_chars, '-'))
