import numpy as np
from PIL import Image
from load_image import ft_load


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert RGB color with numpy broadcasting methond\n
    https://numpy.org/doc/2.3/user/absolute_beginners.html#broadcasting

    Parameters
    ----------
        array (ndarray):
            Expected 3 Dimension Array represent to Image RGB color

    Return
    ------
        ndarray: new ndarray
    """
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Set green, blue channel with numpy broadcasting methond\n
    https://numpy.org/doc/2.3/user/absolute_beginners.html#broadcasting

    Parameters
    ----------
        array (ndarray):
            Expected 3 Dimension Array represent to Image RGB color

    Return
    ------
        ndarray: new ndarray
    """
    new_array = array.copy()
    new_array[:, :, 1:3] = 0
    return new_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Set red, blue channel with numpy broadcasting methond\n
    https://numpy.org/doc/2.3/user/absolute_beginners.html#broadcasting

    Parameters
    ----------
        array (ndarray):
            Expected 3 Dimension Array represent to Image RGB color

    Return
    ------
        ndarray: new ndarray
    """
    new_array = array.copy()
    new_array[:, :, [0, 2]] = 0
    return new_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Set red, green channel with numpy broadcasting methond\n
    https://numpy.org/doc/2.3/user/absolute_beginners.html#broadcasting

    Parameters
    ----------
        array (ndarray):
            Expected 3 Dimension Array represent to Image RGB color

    Return
    ------
        ndarray: new ndarray
    """
    new_array = array.copy()
    new_array[:, :, :2] = 0
    return new_array


def ft_gray(array: np.ndarray) -> np.ndarray:
    """
    calculate average of RGB like (R+G+B)/3
    https://web.stanford.edu/class/cs101/image-6-grayscale-adva.html

    Parameters
    ----------
        array (ndarray):
            Expected 3 Dimension Array represent to Image RGB color

    Return
    ------
        ndarray: new ndarray
    """
    return (np.sum(array, axis=2) / 3).astype(array.dtype)


def combine_images_grid(images: list[Image.Image],
                        cols: int = 3,
                        padding: int = 10,
                        background_color: str = 'white') -> Image.Image:
    """
    combine images to one image

    Parameters
    ----------
        images (list[Image]):
        cols (int): number of image column
        padding (int): padding with space of pixel
        background (str): backgroud color

    Return
    ------
        Image of PIL
    """
    if not images:
        return None

    # find maximum size
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)

    # find number of rows
    rows = (len(images) + cols - 1) // cols

    # calculate size of new Image
    total_width = cols * max_width + (cols + 1) * padding
    total_height = rows * max_height + (rows + 1) * padding

    # create combined image with calculated size
    combined = Image.new('RGB', (total_width, total_height), background_color)

    # paste each image to combined image
    for i, img in enumerate(images):
        row, col = divmod(i, cols)

        # calculate position
        x = padding + col * (max_width + padding)
        y = padding + row * (max_height + padding)

        # some image small, set new position for center grid
        if img.width < max_width:
            x += (max_width - img.width) // 2
        if img.height < max_height:
            y += (max_height - img.height) // 2

        combined.paste(img, (x, y))

    return combined


def main():
    """
    main fo test pimp_image.py
    """
    original = ft_load('../resources/landscape.jpg')
    # print(original)
    invert = ft_invert(original)
    red = ft_red(original)
    green = ft_green(original)
    blue = ft_blue(original)
    gray = ft_gray(original)

    images_np = [original, invert, red, green, blue, gray]
    images = []
    for img in images_np:
        images.append(Image.fromarray(img))
    grid_image = combine_images_grid(images, cols=2)
    grid_image.show()
    # print(ft_invert.__doc__)


if __name__ == '__main__':
    main()
