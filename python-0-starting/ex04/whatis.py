import sys


def whatis(argv) -> None:
    if len(argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif len(argv) < 2:
        return
    try:
        num = int(argv[1])
        print("I'm Odd" if num % 2 else "I'm Even")
    except (ValueError):
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    whatis(sys.argv)
