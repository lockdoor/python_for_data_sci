import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    '''
    give_bmi return list of bmi by calculate (weight / height * height)

    Parameters:
        height (list[float]): list of height in meter
        weight (list[float]): list of weight in kilogram

    Return:
        list[float]: list of bmi
    '''
    try:
        return [float(x[1] / x[0] ** 2)
                for x in np.stack((height, weight), axis=1)]
    except ValueError:
        print("give_bmi: Values error")
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    apply_limit return list of booleen, True if bmi above the limit

    Parameters:
        bmi (list[float]): list of bmi
        limit (int): limit to compare with bmi

    Return:
        list[bool]: list of booleen, True if bmi above the limit
    '''
    return [x > limit for x in bmi]


def main():
    """main for test.py"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
