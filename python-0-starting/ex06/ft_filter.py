def ft_filter(fn, ite) -> list:
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    ft_list = [el for el in ite if fn(el)]
    return ft_list


# print(ft_filter.__doc__)
