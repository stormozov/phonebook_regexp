from fs_tools.abs_path import get_absolute_path
from fs_tools.read_write_csv import read_csv
from phonebook.full_name_parser import parse_full_name
from phonebook.phone_parser import employer_phone_parser

if __name__ == '__main__':
    phonebook_abs_path = get_absolute_path(['data', 'phonebook_raw.csv'])
    phonebook = read_csv(phonebook_abs_path)
    table_header = phonebook[0]

    parsed_full_names: list = parse_full_name(phonebook[1:])
    formatted_phones: list = employer_phone_parser(parsed_full_names)
