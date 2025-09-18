def NULL_not_found(obj: any) -> int:
    if obj is None:
        prefix = "Nothing: None"
    elif isinstance(obj, float) and obj != obj:
        prefix = "Cheese: nan"
    elif isinstance(obj, int) and obj == 0:
        prefix = "Zero: 0"
    elif isinstance(obj, str) and obj == '':
        prefix = "Empty"
    elif isinstance(obj, bool) and not obj:
        prefix = "Fake: False"
    else:
        print("Type not Found")
        return 1
    print(f'{prefix} {type(obj)}')
    return 0


"""
This exercise is experimenting with the idea that
0, NaN, Empty, False is not NULL.
Python is OOP and everything is an object.
"""
