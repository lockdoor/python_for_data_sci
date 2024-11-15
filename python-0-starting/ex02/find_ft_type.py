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
    print (f'{prefix} : {type(obj)}')
    return 42

if __name__ == "__main__":
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10))
