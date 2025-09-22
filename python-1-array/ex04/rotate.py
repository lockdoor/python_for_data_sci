import numpy as np
from load_image import ft_load, ft_zoom
from PIL import Image


def ft_rotate(array: np.ndarray) -> np.ndarray:
    """
    manual_full_transpose_nested_loops
    nested loops with recursive generation by dimensions

    Parameters
    ----------
        arr (ndarray): array 3 dimension represent an image

    Return
    ------
        ndarray
    """
    original_shape = array.shape
    reversed_shape = original_shape[::-1]
    result = np.zeros(reversed_shape, dtype=array.dtype)

    def generate_indices(shapes: np.ndarray, current_indices=[]) -> None:
        """
        Build indices combinations recursive

        Parameters
        ----------
            shapes (ndarray): array slice each dimensions to deepest
            current_indices (list(int)): current original index
        """
        if len(shapes) == 0:
            # Base case: traversal to last dimention in deep
            reversed_indices = tuple(current_indices[::-1])
            # eg: [1, 2, 3] = [3, 2, 1]
            result[reversed_indices] = array[tuple(current_indices)]
            return

        # Recursive case: build indices for dimension present
        current_dim = shapes[0]
        remaining_shapes = shapes[1:]

        for i in range(current_dim):
            generate_indices(remaining_shapes, current_indices + [i])

    generate_indices(list(original_shape))
    return result


def main():
    original = ft_load('../resources/animal.jpeg')
    zoom = ft_zoom(original, x=450, y=100, size=400, mode='L')
    rotate = ft_rotate(zoom)
    img = Image.fromarray(rotate)
    img.show()


if __name__ == '__main__':
    main()
