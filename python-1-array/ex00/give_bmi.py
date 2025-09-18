import numpy as np
import sys


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    '''
    give_bmi return list of bmi by calculate (weight / height * height)
    '''
    try:
        height_np = np.array(height, dtype='f')
        weight_np = np.array(weight, dtype='f')
        bmi: list[float] = []
        for x in np.stack((height_np, weight_np), axis=1):
            bmi.append(float(x[1] / x[0]**2))
        return bmi
    except ValueError:
        print("give_bmi: Values error", file=sys.stderr)
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    apply_limit return list of booleen, True if bmi above the limit
    '''
    try:
        np.array(bmi, dtype='f')
        return [x > limit for x in bmi]
    except ValueError:
        print("apply_limit: Values error", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    # for test.py
    # from give_bmi import give_bmi, apply_limit
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
