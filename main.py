from fs_tools.abs_path import get_absolute_path
from fs_tools.read_write_csv import read_csv

if __name__ == '__main__':
    phonebook_abs_path = get_absolute_path(['data', 'phonebook_raw.csv'])
    contacts_list = read_csv(phonebook_abs_path)

