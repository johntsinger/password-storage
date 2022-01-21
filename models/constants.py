import string


class Literals:
    """String literal variables. Can be modified without break the code"""
    FILE = 'config.ini'
    DEFAULT_SECTION = 'DEFAULT'
    USER_SECTION = 'USER'
    PUNCTUATION = 'punctuation'
    WANTED_PUNCTUATION = 'wanted_punctuation'
    PERCENT_PUNCTUATION = 'percent_punctuation'
    PERCENT_DIGIT = 'percent_digit'
    PERCENT_UPPERCASE = 'percent_uppercase'
    PERCENT_LOWERCASE = 'percent_lowercase'


class Constants:
    """Constants"""
    ALPHABET_LOWERCASE = list(string.ascii_lowercase)
    ALPHABET_UPPERCASE = list(string.ascii_uppercase)
    DIGIT = list(string.digits)
    PUNCTUATION = list(string.punctuation)
