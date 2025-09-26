def precedes(one_string: str, another_string: str) -> str:
    if one_string == another_string:
        return one_string
    elif one_string.lower() < another_string.lower():
        return one_string
    elif one_string.lower() > another_string.lower():
        return another_string