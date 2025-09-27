class Calculator:
    """
    calculatator class for learn operater overload of python
    """

    array: list

    def __init__(self, array) -> object:
        """
        initiate instance

        Parameters:
        -----------
            array (iterable):
        """
        self.array = list(array)

    def __add__(self, object) -> None:
        """plus every element with object argument"""
        self.array = [el + object for el in self.array]
        print(self.__str__())

    def __mul__(self, object) -> None:
        """multiply every element with object argument"""
        self.array = [el * object for el in self.array]
        print(self.__str__())

    def __sub__(self, object) -> None:
        """subtract every element with object argument"""
        self.array = [el - object for el in self.array]
        print(self.__str__())

    def __truediv__(self, object) -> None:
        """divide every element with object argument"""
        try:
            self.array = [el // object for el in self.array]
            print(self.__str__())
        except ZeroDivisionError as e:
            print(f'ZeroDivisionError: {e}')

    def __str__(self):
        return str(self.array)
