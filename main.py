from libs.fs_tools import get_absolute_path, read_csv, write_csv, make_dir
from log_start import logging_start
from libs.phonebook import (
    unify_contacts, parse_full_name, parse_phones, PHONE_PATTERNS
)

if __name__ == '__main__':
    # Start logging.
    logging_start()
    # Create formatted data directory if it doesn't exist.
    make_dir('formatted_data')
    # Get absolute paths to input and output files.
    output_dir_path: str = get_absolute_path([
        'formatted_data',
        'phonebook_formatted.csv'
    ])
    phonebook_abs_path: str = get_absolute_path(['data', 'phonebook_raw.csv'])
    # Read phonebook data.
    phonebook: list[list[str]] = read_csv(phonebook_abs_path)

    # Parse phonebook data and merge contacts with duplicates in the phonebook.
    parse_full_name(phonebook)
    parse_phones(phonebook, PHONE_PATTERNS)
    merged_contacts: list = unify_contacts(phonebook)

    # Write merged contacts to the output file.
    write_csv(output_dir_path, merged_contacts)
