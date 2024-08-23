from libs.fs_tools import get_absolute_path, read_csv
from libs.phonebook import (
    unify_contacts, parse_full_name, parse_phones, PHONE_PATTERNS
)

if __name__ == '__main__':
    # Get the absolute path to the phonebook_raw.csv file.
    phonebook_abs_path: str = get_absolute_path(['data', 'phonebook_raw.csv'])
    phonebook: list[list[str]] = read_csv(phonebook_abs_path)

    # Parse phonebook data and merge contacts with duplicates in the phonebook.
    parse_full_name(phonebook)
    parse_phones(phonebook, PHONE_PATTERNS)
    merged_contacts: list = unify_contacts(phonebook)
