def check_if_integer(value: str) -> bool:
    try:
        int(value)
    except ValueError:
        return False
    return True
