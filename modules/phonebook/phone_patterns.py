import re

PHONE_PATTERNS = {
    'pattern': re.compile(
        r'^(\d)(\d{3})(\d{3})(\d{2})(\d{2})(\d{0,4})$'
    ),
    'replace': r'+7(\2)\3-\4-\5',
    'add': r' доб.\6'
}
