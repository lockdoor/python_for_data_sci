from ft_filter import ft_filter
import sys
import string


def filterstring(sentence: str, amount: int) -> list:
    '''
    filterstriing(sentence: str, amount: int) -> list

    Parameters:
        sentence (str): string to filter word
        amount (int): length of character greater than

    Return:
        Words are separated from each other by space characters.
        Strings do not contain any special character.
    '''
    words = [s for s in sentence.split(" ") if not
             len(list(ft_filter(lambda c: c in string.punctuation, s)))]
    return list(ft_filter(lambda x: len(x) >= amount, words))


def main() -> None:
    '''
    Main function to handle input and call filterstring function
    '''
    if len(sys.argv) != 3:
        print("AssertionError: the argument are bad")
    else:
        print(filterstring(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
