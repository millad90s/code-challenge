import argparse
import sys
from separate_odd_even_numbers import separate_odd_even_numbers
from edit_string import edit_string


def main():
    # Arguments given from command
    params = argparse.ArgumentParser(description='number derivation for even and odd',
                                     usage='%(prog)s -l [Numbers list]', formatter_class=argparse.RawTextHelpFormatter)

    # Add argument for list
    params.add_argument('--list', '-l', nargs='+', type=int,
                        help='list of integers to separate into odd and even numbers')
    # Add argument for Edit string
    params.add_argument('--string', '-s', nargs='+', type=str,
                        help='changes on this string and return the edited input as output')

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
        edited_strs = edit_string(arguments.string)
        print(edited_strs)

    else:
        print("Error: no argument provided!")
        params.print_help()
        sys.exit(1)


# This file is executed as a standalone program
# if the name of the currently executed file is equal to 'main'
if __name__ == '__main__':
    main()
