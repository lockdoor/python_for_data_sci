import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    load dataset as pandas DataFrame

    Parameter
    ---------
        path (str): path of CSV file

    Return
    ------
    - Dataframe: if successed
    - None: if any error occur
    """
    try:
        df = pd.read_csv(path, index_col=0)
        print(f'loading dataset of dimensions {df.shape}')
        return df
    except Exception as e:
        print(e)
        return None


def main():
    """main for load_csv"""
    print(load("../resources/life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
