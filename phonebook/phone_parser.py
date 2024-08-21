import re


def employer_phone_parser(data):
    """Handler of employer's telephone numbers

    This function takes a list of contacts as input, parses and formats the
    phone numbers in each contact, and returns the updated list of contacts.

    Parameters:
        data (list): A list of contacts, where each contact is a list containing
            the contact's information.

    Returns:
        list: The updated list of contacts with formatted phone numbers.
    """
    for contact in data:
        phone: str = contact[5]
        if 'доб.' in phone:
            phone = re.sub(r'\D', '', phone)
            phone = re.sub(
                r'^(\d)(\d{3})(\d{3})(\d{2})(\d{2})(\d{4})$',
                r'+7(\2)\3-\4-\5 доб.\6', phone
            )
        else:
            phone = re.sub(r'\D', '', phone)
            phone = re.sub(
                r'^(\d)(\d{3})(\d{3})(\d{2})(\d{2})$',
                r'+7(\2)\3-\4-\5', phone
            )
        contact[5] = phone

    return data
