def ft_tqdm(lst: range, length: int = 50):

    '''The copy function of tqdm represent progres bar with list range

    Argument:
        lst: list of range
        length: length of progres bar field
    '''

    total = len(lst)
    for i, item in enumerate(lst):
        percent = int(i * 100 / total)

        filled_length = int(length * i // total)
        bar = '=' * filled_length + '>' + ' ' * (length - filled_length - 1)

        represent = f'\r{percent + 1}%|[{bar}]| {item + 1}/{total}'
        print(represent, end="", flush=True)
        yield item
