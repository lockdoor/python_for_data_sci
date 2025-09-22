from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load image as ndarray show the shape and return it

    Parameters
    ----------
        path (str)
            path location of image jpg, png etc.

    Return
    ------
        ndarray
    """
    try:
        img = Image.open(path)
        img_np = np.array(img)
        print(f'The shape of image is: {img_np.shape}')
        return img_np
    except FileNotFoundError:
        print('Error: File Not Found')
        exit(1)
    except UnidentifiedImageError as msg:
        print(f'Error: {msg}')
        exit(1)


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


if __name__ == '__main__':
    print(ft_load('../resources/landscape.jpg'))
