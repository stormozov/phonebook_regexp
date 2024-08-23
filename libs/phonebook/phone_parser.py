import logging
import re

logger = logging.getLogger(__name__)


def parse_phones(contacts: list, pattern: dict) -> list:
    """Parses phone numbers in a list of contacts and returns the updated list.

    This function iterates through each contact in the input list, extracting
    the phone number using the `extract_phone_number()` function. It then
    formats the phone number using `format_phone_number()`, and updates the
    contact using `update_contact()`. Finally, the function returns the input
    list with updated phone numbers.

    Args:
        contacts (list): A list of contacts, where each contact is a list.
        pattern (dict): A dictionary containing the regular expression pattern
            to match phone numbers.

    Returns:
        list: The input list with phone numbers formatted and updated.
    """
    try:
        return [
            update_contact(
                contact_list,
                format_phone_number(
                    extract_phone_number(contact_list), pattern
                )
            ) for contact_list in contacts[1:]
        ]
    except KeyError as e:
        logger.error(f"Missing key in pattern: {e}")
        return []
    except IndexError as e:
        logger.error(f"Invalid index in contacts: {e}")
        return []
    except re.error as e:
        logger.error(f"Invalid regular expression: {e}")
        return []
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return []


def extract_phone_number(contact: list) -> str:
    """Extracts the phone number from a contact record.

    Args:
        contact (list): A list representing a contact record.
            The phone number is assumed to be at index 5.

    Returns:
        str: The phone number from the contact record.
    """
    return contact[5]


def format_phone_number(phone: str, pattern: dict) -> str:
    """Formats the phone number into a single, readable format.

    This function removes all non-numeric characters from a phone number and
    then uses a regular expression to match its pattern. The matching parts
    of the number are replaced with a formatted string that includes the
    country code, area code, and local number. It also formats the extension
    number if available.

    Args:
        phone (str): The phone number to format.
        pattern (dict): A dictionary containing the regular expression pattern
            to match phone numbers.

    Returns:
        str: The formatted phone number.
    """
    phone: str = re.sub(r'\D', '', phone)
    replacement: str = (
        pattern['replace'] + (pattern['add'] if len(phone) > 11 else '')
    )

    return re.sub(pattern['pattern'], replacement, phone)


def update_contact(contacts: list, phone: str) -> list:
    """Updates the contact list with a new phone number.

    Args:
        contacts (list): A list representing a contact record.
        phone (str): The new phone number to update the contact record with.

    Returns:
        list: The updated contact record.
    """
    contacts[5] = phone
    return contacts
