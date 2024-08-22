def parse_full_name(data):
    """ Parses full names into first name, father name and last names.

    Parses the full names in a list of rows and replaces the first three
    elements of each row with the parsed full name.

    Args:
        data (list[list[str]]): The data to parse.

    Returns:
        list[list[str]]: The data with parsed full names.
    """
    for row in data:
        full_name = join_full_name(row)
        row[:3] = split_full_name(full_name)

    return data


def join_full_name(row: list[str]) -> str:
    """Joins a list of strings into a single string.

    Args:
        row (list): The list of strings to join.

    Returns:
        str: The joined string.
    """
    return ' '.join(row[:3]).strip().replace('  ', ' ')


def split_full_name(full_name):
    """Splits a full name into its constituent parts.

    Args:
        full_name (str): The full name to be split.

    Returns:
        list: A list containing the last name (if present), first name, and
            father name (if present).
    """
    parts = full_name.split(' ', 2)
    return [
        parts[0],
        parts[1] if len(parts) > 1 else '',
        parts[2] if len(parts) > 2 else ''
    ]
