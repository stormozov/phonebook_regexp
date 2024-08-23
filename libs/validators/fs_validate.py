def validate_csv_path(csv_path: str) -> None:
    """Validates that the csv_path argument is a non-empty string.

    Args:
        csv_path (str): The path to the CSV file to validators.

    Raises:
        ValueError: If csv_path is not a string or is empty.
    """
    if not isinstance(csv_path, str) or len(csv_path) == 0:
        raise ValueError("csv_path must be a non-empty string")


def validate_contacts_list(contacts_list: list) -> None:
    """Validates that the contacts_list argument is a non-empty list.

    Args:
        contacts_list (list): The list of contacts to validators.

    Raises:
        ValueError: If contacts_list is not a list or is empty.
    """
    if not isinstance(contacts_list, list) or len(contacts_list) == 0:
        raise ValueError("contacts_list must be a non-empty list")


def validate_encoding(encoding: str) -> bool:
    """Validates the input encoding.

    Args:
        encoding (str): The encoding to validators.

    Returns:
        bool: True if the encoding is valid, False otherwise.
    """
    try:
        # Try to encode a string using the input encoding
        "test".encode(encoding)
        return True
    except LookupError:
        # If the encoding is not found, return False
        return False


def validate_path_segments(path_segments: list[str]) -> None:
    """Validates that the path_segments argument is a non-empty list of strings.

    Args:
        path_segments (list[str]): The list of path segments to validators.

    Raises:
        ValueError: If path_segments is not a list or is empty.
        TypeError: If not all elements in path_segments are strings.
    """
    if not isinstance(path_segments, list):
        raise ValueError("path_segments must be a list")
    if len(path_segments) == 0:
        raise ValueError("path_segments must not be empty")
    if not all(isinstance(segment, str) for segment in path_segments):
        raise TypeError("all elements in path_segments must be strings")
