# The second method of this service is to take a string as input
# and perform certain specified changes on this string
# and return the edited input as output.
# The option for this method is -s or --string.


def edit_string(input_strings):
    # Perform the specified changes on input_string & Return edited input
    edited_strings = []
    for i in input_strings:
        string_tmp = i.upper()
        edited_strings.append(string_tmp)
    return edited_strings
