import argparse
import sys
from separate_odd_even_numbers import separate_odd_even_numbers
from edit_string import edit_string


def main():
    # Arguments given from command

    params = argparse.ArgumentParser(
        description='A program for separating even and odd numbers or editing input strings.',
        epilog='Examples:\n\n'
               'Separate even and odd numbers: %(prog)s -l 1 2 3 4 5\n'
               'Edit input strings: %(prog)s -s hello world',
        usage='%(prog)s -s [Input string] [-r] [-sh] [-c]',
        formatter_class=argparse.RawTextHelpFormatter)

    # Add argument for list
    params.add_argument('--list', '-l', nargs='+', type=int,
                        help='list of integers to separate into odd and even numbers')
    # Add argument for Edit string
    params.add_argument('--string', '-s', nargs='+', type=str,
                        help='changes on this string and return the UPPER string input as output')
    params.add_argument('--reverse', '-r', action='store_true',
                        help='changes on this string and return the REVERSE string input as output')
    params.add_argument('--shuffle', '-sh', action='store_true',
                        help='changes on this string and return the SHUFFLE string input as output')
    params.add_argument('--count', '-c', action='store_true',
                        help='changes on this string and return the COUNT string input as output')

    # Check if the list argument is provided
    if len(sys.argv) == 1:
        params.print_help()
        sys.exit(1)

    arguments = params.parse_args()

    if not arguments.list and not arguments.string:
        print("Error: at least one argument is required!")
        params.print_help()
        sys.exit(1)

    # Call function for separate odd and even numbers
    if arguments.list:
        separate_odd_even_numbers(arguments.list)

    elif arguments.string:
        edit_string(arguments.string, reverse=arguments.reverse, shuffle=arguments.shuffle, count=arguments.count)

    else:
        print("Error: no argument provided!")
        params.print_help()
        sys.exit(1)


# This file is executed as a standalone program
# if the name of the currently executed file is equal to 'main'
if __name__ == '__main__':
    main()
