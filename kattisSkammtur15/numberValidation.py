def is_float(string_to_test: str):
    try:
        string_to_test = float(string_to_test)
        return True
    except ValueError:
        return False