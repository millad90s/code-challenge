import argparse
from seprated_odd_even_numbers import seprated_odd_even_numbers

def main():
    # Arguments given from command
    params = argparse.ArgumentParser(description='number derivation for even and odd')
    params.add_argument('--list', '-l', nargs='+', type=int)
    arguments = params.parse_args()

    # Call function for separate odd and even numbers
    seprated_odd_even_numbers(arguments.list)

if __name__ == '__main__':
    main()

