import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, FuncFormatter
from load_csv import load


def _convert_population(val: str) -> int:
    """
    convert value with format k, M to int

    Parameters
    ----------
        val (str):
            string value

    Return
    ------
        int
    """
    if isinstance(val, str):
        val = val.strip().lower()
        if val.endswith('b'):
            return int(float(val[:-1]) * 1_000_000_000)
        elif val.endswith('m'):
            return int(float(val[:-1]) * 1_000_000)
        elif val.endswith('k'):
            return int(float(val[:-1]) * 1_000)
        else:
            return int(float(val))
    return val


def _set_custom_yticks(ax: plt.Axes, data: pd.DataFrame) -> None:
    """
    set custom yticks for this program

    Parameters:
        ax (plt.Axes):
        data (pd.DataFrame):
    """
    max_val = np.max(data)

    if max_val < 10_000:
        step = 2_000
    elif max_val < 100_000:
        step = 20_000
    elif max_val < 1_000_000:
        step = 200_000
    elif max_val < 10_000_000:
        step = 2_000_000
    else:
        step = 20_000_000

    # set locator
    ax.yaxis.set_major_locator(MultipleLocator(step))

    # formatter
    def _format_fn(x: float, pos: int) -> str:
        """
        Custom tick formatter for matplotlib axes.

        Parameters
        ----------
        x : float
            The tick value on the axis (actual numeric value).
        pos : int
            The tick position index (0-based). This is the sequence number
            of the tick, not its numeric value.

        Returns
        -------
        str
            Formatted tick label as a string.
        """
        if x >= 1_000_000:
            return f"{int(x/1_000_000)}M"
        elif x >= 1_000:
            return f"{int(x/1_000)}k"
        return str(int(x))

    ax.yaxis.set_major_formatter(FuncFormatter(_format_fn))


def aff_pop(country_1: str, country_2: str,
            start: int = 1800, end: int = 2050) -> None:
    """
    Display population country_1 versus country_2

    Parameters
    ----------
        country_1 (str):
            country selected
        country_2 (str):
            country selected
        start (int):
            time to start (Year)
        end (int):
            time to end (Year)
    Raise
    -----
        ValueError:
            if wrong argument
        KeyError:
            if not found key in data frame
    """

    # check params
    if country_1.__class__ != str or country_2.__class__ != str:
        raise ValueError('country should is string')

    if start.__class__ != int or end.__class__ != int:
        raise ValueError('start, end must integer')

    # load data
    POPULATION = '../resources/population_total.csv'
    df = load(POPULATION)

    # cleanup data
    df = df.dropna()

    # transpose dataframe and select data for two country
    df = df.T[[country_1, country_2]]
    df.index = df.index.astype(np.int16)

    # slice data from start to end
    df = df.loc[start:end]

    # translate data to integer
    df = df.map(_convert_population)

    # change year index to column
    df = df.reset_index().rename(columns={"index": "Year"})

    # plot line chart
    data_melted = df.melt(id_vars="Year",
                          var_name="Country", value_name="Population")
    g = sns.lineplot(data=data_melted, x="Year", y="Population", hue="Country")
    g.xaxis.set_major_locator(MultipleLocator(40))
    _set_custom_yticks(g, data_melted["Population"].values)
    g.set_title('Population Projections')
    plt.show()


def main():
    """main for aff_pop.py"""
    try:
        aff_pop('Belgium', 'France')
    except KeyboardInterrupt:
        pass
    except KeyError as e:
        print(f'KeyError: {e}')
    except ValueError as e:
        print(f'ValueError: {e}')


if __name__ == '__main__':
    main()
