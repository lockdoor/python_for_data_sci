import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice array from start index to end - 1 (exclude end index)
    if index nagative will count index from last

    Parameters:
        family (list): list for slice
        start (int): index to start with
        end (int): index to end

    Return:
        list: new list
    """
    family_np = np.array(family)
    print('My shape is : ', family_np.shape)
    # slice with [start:end:step], slice will return view of same ndarray
    # https://numpy.org/doc/2.3/user/absolute_beginners.html#array-fundamentals
    # One major difference is that slice indexing of a list copies the elements
    # into a new list, but slicing an array returns a view:
    # an object that refers to the data in the original array.
    # The original array can be mutated using the view.
    family_np = family_np[start:end]
    print('My new shape is: ', family_np.shape)
    return family_np


def main() -> None:
    """
    main for test slice_me
    """
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == '__main__':
    main()
