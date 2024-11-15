def NULL_not_found(obj: any) -> int:
    if obj is None:
        prefix = "Nothing: None"
    elif isinstance(obj, float) and obj != obj:
        prefix = "Cheese: nan"
    elif type(obj) == int and obj == 0:
        prefix = "Zero: 0"
    elif isinstance(obj, str) and obj == '':
        prefix = "Empty"
    elif isinstance(obj, bool) and not obj:
        prefix = "Fake: False"
    else:
        print("Type not Found")
        return 1
    print (f'{prefix} {type(obj)}')
    return 0

# when evaluation copy this to tester.py
if __name__ == "__main__":
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))
