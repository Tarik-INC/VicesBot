import re


def check_format_email(email):

    if (re.search(r".+@.+com", email)):
        raise ValueError("Email read from file isn't in the correct format")
    elif not(re.search(r".+@.+com\s*.", email)):
        raise ValueError(
            "There are two or more email address in the same sentence")
