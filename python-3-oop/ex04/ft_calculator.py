class Calculator:
    """
    Calculator function for vector
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        calculate dotproduct with two vector then print value to console
        Parameters:
        -----------
            V1 (list[float]):
                list of vector
            V2 (list[float]):
                list of vector
        """
        dot = sum([a * b for a, b in zip(V1, V2)])
        print(f'Dot product is: {dot}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        calculate plus two vector then print value to console
        Parameters:
        -----------
            V1 (list[float]):
                list of vector
            V2 (list[float]):
                list of vector
        """
        arr = [a + b for a, b in zip(V1, V2)]
        print(f'Add Vector is: {str(arr)}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        calculate subtract two vector then print value to console
        Parameters:
        -----------
            V1 (list[float]):
                list of vector
            V2 (list[float]):
                list of vector
        """
        arr = [a - b for a, b in zip(V1, V2)]
        print(f'Sous Vector is: {str(arr)}')
