from ft_filter import ft_filter
import sys
import string


def count(l1: str, l2: str) -> int:
    '''count(l1: str, l2: str) -> int\n
return number of characters l1 found in l2'''
    return len(list(filter(lambda c: c in l2, l1)))


def filterstriing(sentence: str, amount: int) -> list:
    '''filterstriing(sentence: str, amount: int) -> list
return list of string fillter by length greater than amount
'''
    words = [el for el in sentence.split(" ")
             if count(el, string.punctuation) == 0]
    return ft_filter(lambda x: len(x) >= amount, words)


def main() -> None:
    '''main() -> None\n
main function
    '''
    if len(sys.argv) != 3:
        return print("AssertionError: the argument are bad")
    try:
        print(filterstriing(sys.argv[1], int(sys.argv[2])))
    except Exception:
        print("AssertionError: the argument are bad")


if __name__ == "__main__":
    main()
