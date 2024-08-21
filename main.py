from fs_tools.abs_path import get_absolute_path
from fs_tools.read_write_csv import read_csv
from phonebook.full_name_parser import parse_full_name

if __name__ == '__main__':
    phonebook_abs_path = get_absolute_path(['data', 'phonebook_raw.csv'])
    contacts_list = read_csv(phonebook_abs_path)

    new_contacts_list = parse_full_name(contacts_list[1:])
