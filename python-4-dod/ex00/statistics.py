from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    ft_statistics is function to make the Mean, Median,
    Quartile (25% and 75%),
    Standard Deviation and Variance according to the **kwargs

    Parameters:
        *args (int | float):
            sequent value for append in list
        **kwargs (Variable keyword arguments. Supported options):
            - toto (str): mean
            - tutu (str): median
            - tata (str): quartile
            - hello (str): standard deviation
            - world (str): variance
    """

    # validate sequent args
    if not args:
        raise ValueError('List of Int or Float is Required')
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError('List of Int or Float is Required')

    # Validate keyword arguments
    allowed_kwargs = {'toto', 'tutu', 'tata', 'hello', 'world'}
    kw = set(kwargs.keys())
    if not kw:
        raise ValueError('Required at lease one kwargs')
    invalid_kwargs = kw - allowed_kwargs
    if invalid_kwargs:
        raise ValueError(f"Invalid keyword arguments: {invalid_kwargs}")

    def get_mean():
        """return mean"""
        return sum(args) / len(args)

    mean: str | None = kwargs.get('toto')
    if mean:
        if mean != 'mean':
            raise ValueError('toto must as mean')
        print(f'mean : {get_mean()}')

    def get_percentile(percent: float):
        """
        get value by percent use (n-1) * percent, like numpy

        Parameter
        ---------
            percent (float):

        Return
        ------
            value of percentile by percent * (n - 1)

        Example
        -------
            get_percentile(0.25):
                return quartile_1
            get_percentile(0.50):
                reuturn quartile_2 (mean)
            get_percentile(0.75):
                return quartile_3
        """
        arr = sorted(args)
        pos: float = percent * (len(arr) - 1)

        if pos.is_integer():
            return arr[int(pos)]
        else:
            lower = int(pos)
            upper = lower + 1
            fraction = pos - lower
            return arr[lower] + fraction * (arr[upper] - arr[lower])

    median: str | None = kwargs.get('tutu')
    if median:
        if median != 'median':
            raise ValueError('tutu must as median')
        q2 = get_percentile(0.5)
        print(f'median : {q2}')

    quartile: str | None = kwargs.get('tata')
    if quartile:
        if quartile != 'quartile':
            raise ValueError('tata must as quartile')
        q1 = get_percentile(0.25)
        q3 = get_percentile(0.75)
        print(f'quartile : {[q1, q3]}')

    def get_variance(sample: bool = False) -> float:
        """
        get variance from *args

        Parameter
        ---------
            sample (bool):
                True for sample, False for population
        Return
        ------
            float:
                variance value
        """
        mean = get_mean()
        return sum([(e - mean) ** 2 for e in args]) / (len(args) - sample)

    std: str | None = kwargs.get('hello')
    if std:
        if std != 'std':
            raise ValueError('hello must as std')
        print(f'std : {get_variance() ** 0.5}')

    var: str | None = kwargs.get('world')
    if var:
        if var != 'var':
            raise ValueError('world must as var')
        print(f'var : {get_variance()}')
