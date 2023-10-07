def convert_to_plural(num_int, noun):
    """
    Convert a singular noun into its plural form based on the given rules.

    Parameters:
    - num_int (int): Non-negative integer.
    - noun (str): Singular noun to be converted.

    Returns:
    str: Plural form of the noun based on the provided number and rules.
    """

    if num_int == 1:
        return f"This is the default case for 1: {num_int} {noun}"
    else:
        if noun[-2:] == 'fe':
            return f"Plural of singular noun {noun} is {num_int} {noun[0:-2]+'ves'}"

        elif noun[-1] == 'y' and noun[-2] not in ['u', 'o', 'e', 'a']:
            return f"Plural of singular noun {noun} is {num_int} {noun[:-1]+'ies'}"

        elif noun[-2:] == 'sh' or noun[-2:] == 'ch':
            return f"Plural of singular noun {noun} is {num_int} {noun +'es'}"

        elif noun[-2:] == 'us':
            return f"Plural of singular noun {noun} is {num_int} {noun[:-2]+'i'}"

        elif noun[-2:] == 'ay' or noun[-2:] =='oy' or noun[-2:] =='ey' or noun[-2:] =='uy':
            return f"Plural of singular noun {noun} is {num_int} {noun + 's'}"

        else:
            return f"Plural of singular noun {noun} is {num_int} {noun + 's'}"

# Taking user input
try:
    num = int(input("Enter the counting of your noun: "))
except ValueError:
    print("You entered a letter here, so please re-run the program")
    exit(0)

noun_ = input("Enter the noun which you want to convert into plural: ")

# Call the function and print the result
result = convert_to_plural(num, noun_)
print(result)