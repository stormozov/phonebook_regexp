import csv

from validators.fs_validate import (
    validate_contacts_list, validate_csv_path, validate_encoding
)


def read_csv(csv_path: str, encoding: str = 'utf-8') -> list:
    """Reads a CSV file and returns its contents as a list of rows.

    Args:
        csv_path (str): The path to the CSV file to read.
        encoding (str): The encoding to use when reading the file.
            Defaults to 'utf-8'.

    Returns:
        list: A list of rows where each row is a list of values.

    Raises:
        ValueError: If csv_path is not a string or is empty.
        FileNotFoundError: If the CSV file does not exist.
    """
    validate_csv_path(csv_path)
    if not validate_encoding(encoding):
        raise ValueError(f'Invalid encoding: {encoding}')

    csv_data = read_csv_file(csv_path, encoding)
    return parse_csv_data(csv_data)


def read_csv_file(csv_path: str, encoding: str = 'utf-8') -> str:
    """Reads a CSV file and returns its contents as a string.

    Args:
        csv_path (str): The path to the CSV file to read.
        encoding (str): The encoding to use when reading the file.

    Returns:
        str: The contents of the CSV file as a string.

    Raises:
        ValueError: If csv_path is not a string or is empty.
        FileNotFoundError: If the CSV file does not exist.
    """
    try:
        with open(csv_path, encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise ValueError(f'Файл "{csv_path}" не существует')


def parse_csv_data(csv_data: str) -> list:
    """This function parses a CSV data string into a list of rows.

    Args:
        csv_data (str): A string containing CSV data.

    Returns:
        list: A list of rows where each row is a list of values.
    """
    rows = csv.reader(csv_data.splitlines(), delimiter=',')
    return list(rows)


def write_csv(csv_path: str, contacts_list: list) -> None:
    """Writes a CSV file from a list of contacts.

    Args:
        csv_path (str): The path to the CSV file to write.
        contacts_list (list): A list of contacts where each contact is a list
            of values.

    Raises:
        ValueError: If csv_path is not a string or is empty.
        ValueError: If contacts_list is not a list or is empty.
    """
    validate_csv_path(csv_path)
    validate_contacts_list(contacts_list)
    write_rows_to_csv(csv_path, contacts_list)


def write_rows_to_csv(csv_path: str, rows: list, encoding: str = 'utf-8') \
        -> None:
    """Writes a list of rows to a CSV file.

    Args:
        csv_path (str): The path to the CSV file to write.
        rows (list): A list of rows where each row is a list of values.
        encoding (str): The encoding to use when writing the file.
            Defaults to 'utf-8'.

    Returns:
        None

    Raises:
        IOError: If an I/O error occurs while writing to the file.
        csv.Error: If an error occurs while writing to the CSV file.
    """
    try:
        with open(csv_path, 'w', encoding=encoding) as f:
            datawriter = csv.writer(f, delimiter=',')

            try:
                datawriter.writerows(rows)
            except csv.Error as e:
                raise csv.Error(f'Error writing to CSV file: {e}')
    except IOError as e:
        raise IOError(f'Error writing to CSV file: {e}')
