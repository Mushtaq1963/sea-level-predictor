import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    try:
        plt.clf()  # Clear the current figure to avoid overlap
        
        # Read data from file
        df = pd.read_csv('D:/global-average-sea-level-change/boilerplate-sea-level-predictor/epa-sea-level.csv')
        
        # Check if the expected columns are in the dataset
        print("Columns in CSV:", df.columns)
        print("First 8 rows of data:")
        print(df.head(8))

        # Check for missing values
        if df.isnull().any().any():
            print("Warning: Missing values found in the dataset.")
        
        # Create scatter plot
        plt.figure(figsize=(10, 5))
        plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label="Data Points")
        
        # Create first line of best fit (1880-2050)
        slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
        years_ext = pd.Series([i for i in range(1880, 2051)])
        
        # Debug: print values for the first line of best fit
        print(f"Slope (1880-2050): {slope}, Intercept (1880-2050): {intercept}")
        print("Years for line of best fit:", years_ext.head())
        
        plt.plot(years_ext, intercept + slope * years_ext, 'r', label="Fit (1880-2050)")
        
        # Create second line of best fit (2000-2050)
        df_recent = df[df['Year'] >= 2000]
        slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
        years_recent = pd.Series([i for i in range(2000, 2051)])
        
        # Debug: print values for the second line of best fit
        print(f"Slope (2000-2050): {slope_recent}, Intercept (2000-2050): {intercept_recent}")
        print("Years for recent line of best fit:", years_recent.head())
        
        plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'green', label="Fit (2000-2050)")

        # Add labels and title
        plt.xlabel("Year")
        plt.ylabel("Sea Level (inches)")
        plt.title("Rise in Sea Level")
        plt.legend()

        # Save plot and show
        plt.savefig('sea_level_plot.png')
        plt.show()  # This will display the plot
        plt.close()  # Close the plot after showing it
        return plt.gca()

    except Exception as e:
        print(f"Error: {e}")

# Call the function to draw the plot
draw_plot()

