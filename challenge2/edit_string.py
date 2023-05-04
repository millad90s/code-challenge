# The second method of this service is to take a string as input
# and perform certain specified changes on this string
# and return the edited input as output.
# The option for this method is -s or --string.
import random


def edit_string(input_strings,reverse=False, shuffle=False, count=False):
    # Perform the specified changes on input_string & Return edited input
    edited_strings = []
    for i in input_strings:
        string_tmp = i.upper()
        edited_strings.append(string_tmp)
    if reverse:
        edited_strings = edited_strings[::-1]
    if shuffle:
        edited_strings = ''.join((random.sample(edited_strings, len(edited_strings))))
    if count:
        edited_strings = f"The string has {len(edited_strings)} characters."

    print("Result: ",edited_strings)



