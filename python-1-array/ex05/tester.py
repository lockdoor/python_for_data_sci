from load_image import ft_load
from pimp_image import (ft_invert, ft_red,
                        ft_green, ft_blue, ft_gray, combine_images_grid)
from PIL import Image


def main():
    """
    main fo test pimp_image.py
    """
    original = ft_load('../resources/landscape.jpg')
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


if __name__ == '__main__':
    main()
