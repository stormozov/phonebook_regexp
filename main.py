from fs_tools.abs_path import get_absolute_path
from fs_tools.csv_utils import read_csv
from phonebook.full_name_parser import parse_full_name
from phonebook.phone_parser import parse_phones
from phonebook.duplicate_remover import unify_contacts
from phonebook.phone_patterns import PHONE_PATTERNS

if __name__ == '__main__':
    # Get the absolute path to the phonebook_raw.csv file.
    phonebook_abs_path: str = get_absolute_path(['data', 'phonebook_raw.csv'])
    phonebook: list[list[str]] = read_csv(phonebook_abs_path)

    # Parse phonebook data and merge contacts with duplicates in the phonebook.
    parse_full_name(phonebook)
    parse_phones(phonebook, PHONE_PATTERNS)
    merged_contacts: list = unify_contacts(phonebook)
