from time import gmtime, strftime, time


if __name__ == '__main__':
    t = time()
    print('Seconds since ', end="")
    print(strftime("%B %-d, %Y", gmtime(0)), end="")
    print(f': {t:,.4f} or {t:.2e} in scientific notation')
    print(strftime("%b %d %Y", gmtime()))


"""
For time formatting options, see:
https://docs.python.org/3/library/time.html

For format string syntax, see:
https://docs.python.org/3/library/string.html#format-string-syntax
"""
