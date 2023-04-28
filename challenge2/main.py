import argparse
from even_odd import separate_even_odd_numbers
from edit_string import edit_string
from get_ip import get_public_and_internal_ip
from check_email import check_social_network

parser = argparse.ArgumentParser(description='Python service that performs various tasks.')
subparsers = parser.add_subparsers(dest='command', help='Available commands')

# Method 1: Separate even and odd numbers
even_odd_parser = subparsers.add_parser('even_odd', help='Separate even and odd numbers')
even_odd_parser.add_argument('-l', '--list', nargs='+', type=int, required=True, help='List of numbers')
def even_odd_handler(args):
    even_numbers, odd_numbers = separate_even_odd_numbers(args.list)
    print('Even numbers:', even_numbers)
    print('Odd numbers:', odd_numbers)

# Method 2: Edit a string
edit_string_parser = subparsers.add_parser('edit_string', help='Edit a string')
edit_string_parser.add_argument('-s', '--string', type=str, required=True, help='Input string')
def edit_string_handler(args):
    edited_string = edit_string(args.string)
    print('Edited string:', edited_string)

# Method 3: Get public and internal IP
get_ip_parser = subparsers.add_parser('get_ip', help='Get public and internal IP')
def get_ip_handler(args):
    public_ip, internal_ip = get_public_and_internal_ip()
    print('Public IP:', public_ip)
    print('Internal IP:', internal_ip)

# Method 4: Check email on a social network
check_email_parser = subparsers.add_parser('check_email', help='Check email on a social network')
check_email_parser.add_argument('-e', '--email', type=str, required=True, help='Input email')
check_email_parser.add_argument('-n', '--network', type=str, required=True, help='Social network to check')
def check_email_handler(args):
    result = check_social_network(args.email, args.network)
    if result:
        print(args.email, 'has an active account on', args.network)
    else:
        print(args.email, 'does not have an active account on', args.network)

# Parse arguments and run command
args = parser.parse_args()
if args.command == 'even_odd':
    even_odd_handler(args)
elif args.command == 'edit_string':
    edit_string_handler(args)
elif args.command == 'get_ip':
    get_ip_handler(args)
elif args.command == 'check_email':
    check_email_handler(args)
else:
    parser.print_help()
