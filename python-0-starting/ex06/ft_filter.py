def ft_filter(fn, ite):
    '''filter(function or None, iterable) --> filter object \n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    '''
    if ite is None:
        ite = []
    if fn is None:
        for el in ite:
            if el:
                yield el
    else:
        for el in ite:
            if fn(el):
                yield el
