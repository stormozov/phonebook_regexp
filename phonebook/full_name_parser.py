def parse_full_name(data):
    for row in data:
        full_name = ' '.join(row[:3])
        full_name = full_name.strip()
        full_name = full_name.replace('  ', ' ')
        parts = full_name.split(' ')

        if len(parts) == 3:
            last_name, first_name, father_name = parts
        else:
            last_name, first_name, father_name = parts + [''] * (3 - len(parts))

        row[:3] = [last_name, first_name, father_name]

    return data
