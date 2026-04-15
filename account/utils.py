import re

def validate_phone_number(phone):
    pattern = r'^(\+\d{1,3}[-]?)?\d{10, 12}$'
    return bool(re.match(pattern, phone))