import string
import sys

'''
__doc__ format for functions:

Description of the function
Parameters:
    param1 (type): description
    param2 (type): description
Returns:
    return_type: description
'''


def building(w: str) -> None:
    '''
    Print amount of characters
    Parameters:
        w (str): string to analyze
    '''
    print("The text contains", len(w), "characters")
    print(len([c for c in w if c in string.ascii_uppercase]), "upper letters")
    print(len([c for c in w if c in string.ascii_lowercase]), "lower letters")
    print(len([c for c in w if c in string.punctuation]), "punctuation marks")
    print(len([c for c in w if c in string.whitespace]), "spaces")
    print(len([c for c in w if c in string.digits]), "digits")


def main() -> None:
    '''
    Main function to handle input and call building function
    '''
    if len(sys.argv) > 2:
        print("AssertionError: Wrong number of agrument")
    elif len(sys.argv) == 2:
        building(sys.argv[1])
    else:
        print("What is the text to count?")
        input_text = sys.stdin.readline()
        building(input_text)


if __name__ == "__main__":
    main()
