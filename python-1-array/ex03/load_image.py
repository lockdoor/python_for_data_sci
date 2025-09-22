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


if __name__ == '__main__':
    print(ft_load('../resources/landscape.jpg'))
