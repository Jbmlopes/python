def main():
    plate = input("Plate: ")
    if is_valid(plate): #function to tell me if the plate is valid
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # checks each of rules

    if length_right(s) == False:
        return False

    if start_right(s) == False:
        return False

    if characters_right(s) == False:
        return False

    if numbers_right(s) == False:
        return False

    return True # If everything before is right


def length_right(s):
 # “start with at least two letters.”, “… vanity plates may contain a maximum of 6 characters”
    if len(s) < 2 or len(s) > 6:
        return False
    return True


def start_right(s):
    # the first two characters must be letters
    if s[0:2].isalpha(): #isalpha(): function to verify if string is exclusively alfabet letters
        return True
    return False


def characters_right(s):
    # no periods, spaces, punctuation
    if s.isalnum(): #isalnum(): checks if all characters in a string are letters or numbers.
        return True
    return False

def numbers_ok(s):
    # numbers only at the end, and the first number can't be 0? I go through the plate one character at a time?

main()
