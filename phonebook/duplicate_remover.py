def unify_contacts(data: list) -> list:
    """Merges duplicate records in a list of contact information.

    The function takes a list of contact information and returns a list of
    unique contact information with merged phone numbers and emails.

    Args:
        data (list): A list of contact information, where each contact is a list
            of strings.

    Returns:
        list: A list of unique contact information with merged phone numbers
            and emails.
    """
    unique_contacts = {}

    for contact in data:
        name_and_surname = tuple(contact[:2])
        existing_contact = unique_contacts.get(name_and_surname)

        if existing_contact:
            existing_contact[4] += contact[4]
            existing_contact[5] += contact[5]
            existing_contact[6] += contact[6]
        else:
            unique_contacts[name_and_surname] = contact

    return list(unique_contacts.values())
