import argparse
import sys
from separate_odd_even_numbers import separate_odd_even_numbers


def main():
    # Arguments given from command
    params = argparse.ArgumentParser(description='number derivation for even and odd',
                                     usage='%(prog)s -l [Numbers list]', formatter_class=argparse.RawTextHelpFormatter)

    # Add argument for list
    params.add_argument('--list', '-l', nargs='+', type=int,
                        help='list of integers to separate into odd and even numbers')

    # Check if the list argument is provided
    if len(sys.argv) == 1:
        params.print_help()
        sys.exit(1)

    arguments = params.parse_args()

    if not arguments.list:
        print("Error: list argument is missing!")
        params.print_help()
        sys.exit(1)

    # Call function for separate odd and even numbers
    separate_odd_even_numbers(arguments.list)


# This file is executed as a standalone program
# if the name of the currently executed file is equal to 'main'
if __name__ == '__main__':
    main()
