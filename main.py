from fs_tools.abs_path import get_absolute_path
from fs_tools.read_write_csv import read_csv
from phonebook.full_name_parser import parse_full_name
from phonebook.phone_parser import employer_phone_parser
from phonebook.duplicate_remover import unify_contacts

if __name__ == '__main__':
    phonebook_abs_path: str = get_absolute_path(['data', 'phonebook_raw.csv'])
    phonebook: list[list[str]] = read_csv(phonebook_abs_path)
    table_header: list[str] = phonebook[0]

    parse_full_name(phonebook[1:])
    employer_phone_parser(phonebook[1:])
    merged_contacts: list = unify_contacts(phonebook[1:])
