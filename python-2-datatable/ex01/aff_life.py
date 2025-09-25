import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import MultipleLocator


def aff_life(country: str) -> None:
    """
    displays the country population information of the country

    Parameters
    ----------
        country (str):
            country selected

    Raise
    -----
        KeyError:
            if not found key in data frame
        AttributeError:
            if no dataframe
    """

    # load data
    LIFE = '../resources/life_expectancy_years.csv'
    df: pd.DataFrame = load(LIFE)

    # select country sr is pd.series
    sr: pd.Series = df.loc[country]

    g = sns.lineplot(sr)
    g.xaxis.set_major_locator(MultipleLocator(40))
    g.set_title(f'{country} Life expectancy Projections')
    g.set_ylabel('Life expectancy')
    g.set_xlabel('Year')
    plt.show()


def main():
    """main for aff_life.py"""
    try:
        aff_life('Thailand')
    except KeyboardInterrupt:
        pass
    except KeyError as e:
        print(f'KeyError: {e}')
    except AttributeError as e:
        print(f'AttributeError: {e}')


if __name__ == '__main__':
    main()
