def square(x: int | float) -> int | float:
    """Calculate x squared (x²)"""
    # validate
    if not isinstance(x, (int, float)):
        raise ValueError('x must int or float')

    return x ** 2


def pow(x: int | float) -> int | float:
    """Calculate x to the power of x (x^x)"""
    # validate
    if not isinstance(x, (int, float)):
        raise ValueError('x must int or float')

    return x ** x


def outer(x: int | float, function) -> object:
    """Apply function repeatedly"""
    count = 0

    def inner() -> float:
        # nonlocal is referrence enclosing scope
        # if not nonlocal python will treat variable readonly
        nonlocal count
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count

    return inner


def main():
    """main for in_out.py"""
    counter = outer(3, square)
    print(counter())
    print(counter())
    print(counter())
    counter = outer(1.5, pow)
    print(counter())
    print(counter())
    print(counter())


if __name__ == '__main__':
    main()
