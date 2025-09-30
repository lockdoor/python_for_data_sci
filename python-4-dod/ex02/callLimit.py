from typing import Any


def callLimit(limit: int):
    """
    https://realpython.com/primer-on-python-decorators/\n
    This function use for decorator, it wrap other funcnion then call it inside

    Parameter
    ---------
        limit (int):
            limit time to can call the function

    Return
    ------
        function object with wrap function below
    """
    count = 0

    def callLimiter(function):
        """inner function"""
        def limit_function(*args: Any, **kwds: Any):
            """inner function"""
            nonlocal count
            if count >= limit:
                print(f'Error: {function} call too many times {count}')
            else:
                function()

            count += 1
        return limit_function

    return callLimiter
