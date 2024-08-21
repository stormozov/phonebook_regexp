import csv


def read_csv(csv_path: str, encoding: str = "utf-8") -> list:
    """Reads a CSV file and returns its contents as a list of lists.

    Args:
        csv_path: The path to the CSV file to read.
        encoding: The encoding of the CSV file, defaults to utf-8.

    Returns:
        The contents of the CSV file as a list of lists.
    """
    with open(csv_path, encoding=encoding) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    return contacts_list


def write_csv(csv_path: str, contacts_list: list) -> None:
    """Writes a list of lists to a CSV file.

    Args:
        csv_path (str): The path to the CSV file to write.
        contacts_list (list): The data to write to the CSV file.
            Each inner list represents a row in the CSV file.

    Returns:
        None
    """
    with open(csv_path, "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
