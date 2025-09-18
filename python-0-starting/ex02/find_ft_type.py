def all_thing_is_obj(obj: any) -> int:
    if isinstance(obj, list):
        prefix = "List"
    elif isinstance(obj, tuple):
        prefix = "Tuple"
    elif isinstance(obj, set):
        prefix = "Set"
    elif isinstance(obj, dict):
        prefix = "Dict"
    elif isinstance(obj, str):
        prefix = f'{obj} is in the kitchen'
    else:
        print("Type not found")
        return 42
    print(f'{prefix} : {type(obj)}')
    return 42
