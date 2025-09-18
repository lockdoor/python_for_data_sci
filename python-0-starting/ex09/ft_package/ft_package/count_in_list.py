from typing import TypeVar
T = TypeVar('T')


def count_in_list(ls: list[T], el: T) -> int:
    """
    Count occurrences of `el` in `ls`.

    Args:
        ls (list[T]): The list to search.
        el (T): The element to count.

    Returns:
        int: The number of occurrences of `el` in `ls`.
    """
    return ls.count(el)
