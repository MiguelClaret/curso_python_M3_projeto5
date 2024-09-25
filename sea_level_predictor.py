import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea_level_predictor.py')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Sea Level')

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended_all = np.arange(df['Year'].min(), 2051, 1)
    sea_level_predicted_all = intercept_all + slope_all * years_extended_all
    plt.plot(years_extended_all, sea_level_predicted_all, color='r', label='Best Fit Line (All Data)')

    # Create second line of best fit
    df_since_2000 = df[df['Year'] >= 2000]
    slope_since_2000, intercept_since_2000, _, _, _ = linregress(df_since_2000['Year'], df_since_2000['CSIRO Adjusted Sea Level'])
    years_extended_since_2000 = np.arange(2000, 2051, 1)
    sea_level_predicted_since_2000 = intercept_since_2000 + slope_since_2000 * years_extended_since_2000
    plt.plot(years_extended_since_2000, sea_level_predicted_since_2000, color='g', label='Best Fit Line (Since 2000)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
