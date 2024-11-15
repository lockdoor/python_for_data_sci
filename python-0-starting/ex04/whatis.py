import sys

def whatis(argv):
    if len(argv) > 2:
        return print("AssertionError: more than one argument is provided")
    elif len(argv) < 2:
        return print("AssertionError: expect one argument is number")
    try:
        num = int(argv[1])
        print ("I'm EVEN" if num % 2 else "I'm Odd")
    except (ValueError):
        print ("AssertionError: argument is not an integer")

if __name__ == "__main__":
    whatis(sys.argv)
