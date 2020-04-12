
def main():
    MINIMUM_LENGTH = 7
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get and validates password considering characters"""
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Your password should be of 7 characters")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    """Print asterisks of the same number of characters ."""
    print('*' * len(sequence))


main()