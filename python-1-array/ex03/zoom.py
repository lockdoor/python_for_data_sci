import numpy as np
from load_image import ft_load
from PIL import Image


def ft_zoom(arr: np.ndarray, x: int = 0,
            y: int = 0, size: int = 0, mode: str = "RGB") -> np.ndarray:
    """
    Slicing array with x, y coordinate end with plus size or rest of pixel

    Parameters
    ----------
        arr (ndarray): array 3 dimension represent an image
        x (int): start column of pixel
        y (int): start row of pixel
        size (int): end of pixel
        mode (str): allow mode 'RGB' color and 'L' for grayscale
    Return
    ------
        ndarray: new ndarray with square size
    """

    if arr.ndim != 3:
        raise ValueError('Allow only 3 dimension array')

    if arr.dtype != np.uint8:
        raise ValueError('Array type must as np.uint8')

    if mode != "RGB" and mode != "L":
        raise ValueError('mode can use only RGB or L')

    if x < 0 or y < 0 or size < 0:
        raise ValueError('(x, y, size): must positive int number')

    # if end if out of range numpy will slice to last element
    zoom = arr[y: y + size, x: x + size]

    if not zoom.size:
        raise ValueError('size of array is 0 course wrong coordinate (x, y)')

    if mode == 'L':
        # np.mean() return np.dtype is float64
        # use astype for cast type to original type
        return np.mean(zoom, axis=2).astype(arr.dtype)
    return zoom.copy()


def main():
    """
    main for test zoom()
    """
    np.set_printoptions(
        edgeitems=3      # show 3 elements first and last
    )
    original = ft_load('../resources/animal.jpeg')
    print(original)
    z = ft_zoom(original, x=450, y=100, size=400, mode='L')
    print(f'New shape after slicing: {z.shape}')
    print(z)
    img = Image.fromarray(z)
    img.show()


if __name__ == '__main__':
    main()
