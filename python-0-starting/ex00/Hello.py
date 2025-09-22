ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list is mutable we can change it by index
ft_list[1] = "world!"

# tuple is immutable cannot be changed to change it should change to list
lst = list(ft_tuple)
lst[1] = "Thailand!"
ft_tuple = tuple(lst)

# set is unordered collection of unique elements
# so we cannot change it by index but we can add or remove elements
ft_set.remove("tutu!")
ft_set.add("Bangkok!")

# dictionary is mutable we can change it by key
ft_dict["Hello"] = "42Bangkok!"

if __name__ == '__main__':
    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)

"""
Python sets are inherently unordered collections of unique elements.
This means that the elements within a set do not maintain any specific order,
and their arrangement may vary when iterating over the set or printing it.
"""
