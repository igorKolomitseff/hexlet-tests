def capitalize(text: str) -> str:
    """Returns a string that starts with a capital letter.

    Args:
        text: Any string.

    Returns:
        str: A string whose first letter is uppercase.
    """

    if text == '':
        return ''
    
    first_char = text[0].upper()
    rest_substring = text[1:]

    return f'{first_char}{rest_substring}'