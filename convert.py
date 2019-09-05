# IST220-01
# Yuan Fu
# Lab 1 - Convert Decimal to Binary

# Note: I write this program in Python 3

import sys

help_message = '''#######################################
Welcome to the Decimal-Binary converter!
#######################################

This program aims at providing you the smoothest experience
of converting decimal numbers from and to binary numbers.


### How to use the program ###

Each time when you are prompted for a command like this
(bar represents the cursor):

[00;32;1m==>>> |[0m

Enter a number, a space and letter "d" (for decimal) or "b" (for binary),
then hit enter. For example:

[00;32;1m==>>> 1011 d[0m

This command converts 1011 from binary to decimal.
Note that the program only accept positive integers.


To quit the program, type "quit" and hit enter:

[00;32;1m==>>> quit[0m


To show this help again, type "help" and hit enter:

[00;32;1m==>>> help[0m

#######################################

'''


def decimal_to_binary(decimal):
    """Converts decimal to binary.

Arguments:
- decimal (str): The number.

Returns:
- string: the binary number in string format.
"""
    # setup & check
    digit_list = []
    try:
        left_over = int(decimal)
    except ValueError:
        print('!!! Not a valid number: %s' % decimal)
        return 'N/A'

    while left_over >= 0:
        if left_over == 0:
            break
        remainder = left_over % 2
        digit_list.insert(0, str(remainder))
        left_over = left_over // 2
    if len(digit_list) == 0:
        return '0'
    else:
        return ''.join(digit_list)

def is_binary(number):
    """Validates number as a binary number.

Arguments:
- number (str): The number.

Returns:
- bool: True if valid, otherwise False."""
    for digit in number:
        if digit != '1' and digit != '0':
            return False
    return True


def binary_to_decimal(binary):
    """Converts binary to decimal.

Arguments:
- binary (str): the number.
    
Returns:
- string: the decimal number in string format.
"""
    # setup & check
    if not is_binary(binary):
        print('!!! Not a validate binary number: %a' % binary)
        return 'N/A'

    binary = list(reversed(binary))
    decimal = 0
    for digit_index in range(len(binary)):
        digit = binary[digit_index]
        if digit == '0' and digit_index == 0:
            # otherwise 0 ** 0 = 1
            continue
        decimal += (2 * int(digit))**digit_index
    return str(decimal)


def convert(number, specifier):
    """Convert number between decimal and binary depends on specifier.

Specifier can be 'b' for binary or 'd' for decimal.
"""
    # decimal -> binary
    if specifier == 'b':
        return decimal_to_binary(number)
    # binary -> decimal
    elif specifier == 'd':
        return binary_to_decimal(number)


def prompt_and_process():
    """Prompt user and execute command."""
    # prompt
    command = input('[00;32;1m==>>> [0m').lstrip('==>>> ')

    # handle special command
    if command == 'help':
        print_help()
    elif command == 'quit':
        quit()
    # handle conversion command
    else:
        command_list = command.rstrip(' ').lstrip(' ').split(' ')
        if len(command_list) < 2:
            return
        number = command_list[0]
        specifier = command_list[1]
        result = convert(number, specifier)
        if specifier == 'd':
            from_ = 'Binary'
            to_ = 'Decimal'
        elif specifier == 'b':
            from_ = 'Decimal'
            to_ = 'Binary'
        print('''
{}: {}
{}: {}
'''.format(from_, number, to_, result))


def print_help():
    """Print help message."""
    print(help_message)


def quit():
    """Quit the program."""
    sys.exit(0)


def app():
    """The main program."""
    print_help()
    while True:
        prompt_and_process()


if __name__ == '__main__':
    app()
