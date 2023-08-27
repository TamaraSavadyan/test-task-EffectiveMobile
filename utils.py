def check_if_integer(value: str) -> bool:
    '''
    Checks if a given string can be converted to an integer.

    Parameters:
        value (str): The string value to check.

    Returns:
        bool: True if the string can be converted to an integer, False otherwise.
    '''
    try:
        int(value)
    except ValueError:
        return False
    return True
