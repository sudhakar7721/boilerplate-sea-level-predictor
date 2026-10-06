import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from CSV file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create first line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years = pd.Series(
        range(
            df["Year"].min(),
            2051
        )
    )

    ax.plot(
        years,
        intercept + slope * years
    )

    # Create second line of best fit using data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = pd.Series(
        range(
            2000,
            2051
        )
    )

    ax.plot(
        years_recent,
        intercept_recent + slope_recent * years_recent
    )

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save the plot
    fig.savefig("sea_level_plot.png")

    # Return Axes for the freeCodeCamp tests
    return ax