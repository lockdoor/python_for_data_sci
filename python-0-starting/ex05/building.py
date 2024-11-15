import string
import sys


def count(l1: str, l2: str) -> int:
    '''
    count(l1: str, l2: str) -> int\n
    return number of characters l1 found in l2
    '''
    return len(list(filter(lambda c: c in l2, l1)))


def main(word) -> None:
    '''print amount of characters'''
    print("The text contains", len(word), "characters")
    print(count(word, string.ascii_uppercase), "upper letters")
    print(count(word, string.ascii_lowercase), "lower letters")
    print(count(word, string.punctuation), "punctuation marks")
    print(count(word, string.whitespace), "spaces")
    print(count(word, string.digits), "digits")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: Wrong number of agrument")
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        try:
            main(input("What is the text to count?\n") + '\n')
        except EOFError:
            pass
