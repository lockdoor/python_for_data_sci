from ft_package import count_in_list


if __name__ == "__main__":
    my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    element = 'apple'
    count = count_in_list(my_list, element)
    print(f"The element '{element}' appears {count} times in the list.")
