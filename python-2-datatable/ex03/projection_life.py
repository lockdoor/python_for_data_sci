from load_csv import load
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def projection_life(year: int) -> None:
    """
    projection of life expectancy in relation to the gross national
    product of the year for each country.

    Parameters
    ----------
        year (int):

    Raise
    -----
        KeyError: if not found key in data frame
    """

    LIFE_EXPECT = '../resources/life_expectancy_years.csv'
    INCOME = '../resources/\
    income_per_person_gdppercapita_ppp_inflation_adjusted.csv'

    # import data
    life_df = load(LIFE_EXPECT)
    income_df = load(INCOME)

    # clean data
    life_df = life_df.dropna()
    income_df = income_df.dropna()

    # change columns to int
    life_df.columns = life_df.columns.astype(int)
    income_df.columns = income_df.columns.astype(int)

    # get series by year
    life_series = life_df[year]
    income_series = income_df[year]

    # create new dataFrame
    df = pd.DataFrame({'life': life_series, 'income': income_series})

    # clean data again
    df = df.dropna()

    # plot
    sns.scatterplot(df, x='income', y='life')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title(year)
    plt.show()


def main():
    """
    main for projection_life.py
    """
    try:
        projection_life(1900)
    except KeyboardInterrupt:
        pass
    except KeyError as e:
        print(f'KeyError: {e}')


if __name__ == '__main__':
    main()
