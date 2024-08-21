import re


def employer_phone_parser(data: list) -> list:
    """Parses phone numbers in a list of contacts and returns the updated list.

    This function iterates through each contact in the input list, extracting
    the phone number using the `extract_phone_number()` function. It then
    formats the phone number using `format_phone_number()`, and updates the
    contact using `update_contact()`. Finally, the function returns the input
    list with updated phone numbers.

    Args:
        data (list): A list of contacts, where each contact is a list.

    Returns:
        list: The input list with phone numbers formatted and updated.
    """
    for contact in data:
        phone = extract_phone_number(contact)
        formatted_phone = format_phone_number(phone)
        update_contact(contact, formatted_phone)
    return data


def extract_phone_number(contact: list) -> str:
    """Extracts the phone number from a contact record.

    Args:
        contact (list): A list representing a contact record.
            The phone number is assumed to be at index 5.

    Returns:
        str: The phone number from the contact record.
    """
    return contact[5]


def format_phone_number(phone: str) -> str:
    """Formats the phone number into a single, readable format.

    This function removes all non-numeric characters from a phone number and
    then uses a regular expression to match its pattern. The matching parts
    of the number are replaced with a formatted string that includes the
    country code, area code, and local number. It also formats the extension
    number if available.

    Args:
        phone (str): The phone number to format.

    Returns:
        str: The formatted phone number.
    """
    phone = re.sub(r'\D', '', phone)

    pattern = r'^(\d)(\d{3})(\d{3})(\d{2})(\d{2})(\d{0,4})$'
    replacement = r'+7(\2)\3-\4-\5' + (r' доб.\6' if len(phone) > 11 else '')

    return re.sub(pattern, replacement, phone)


def update_contact(contact: list, phone: str) -> list:
    """Updates the contact list with a new phone number.

    Args:
        contact (list): A list representing a contact record.
        phone (str): The new phone number to update the contact record with.

    Returns:
        list: The updated contact record.
    """
    contact[5] = phone
    return contact
