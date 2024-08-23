from .duplicate_remover import unify_contacts
from .full_name_parser import parse_full_name
from .phone_parser import parse_phones
from .phone_patterns import PHONE_PATTERNS

__all__ = [
    "unify_contacts",
    "parse_phones",
    "parse_full_name",
    "PHONE_PATTERNS"
]
