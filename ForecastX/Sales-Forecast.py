# Import required libraries for data handling and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# File name of dataset
DATA_FILE = "data.csv"

# Number of months for moving average calculation
MOVING_AVERAGE_MONTHS = 3


def load_sales_data(file_path):
    """Load the sales dataset and convert the date column to datetime format."""
    # Read CSV file into pandas DataFrame
    sales_data = pd.read_csv(file_path)
    
    # Convert 'date' column to proper datetime format
    sales_data["date"] = pd.to_datetime(sales_data["date"])
    
    return sales_data


def print_dataset_overview(sales_data):
    """Display basic information about the dataset."""
    
    # Show first 5 rows of dataset
    print("First 5 Rows:")
    print(sales_data.head())

    # Show structure (columns, data types, non-null values)
    print("\nDataset Info:")
    sales_data.info()

    # Show statistical summary (mean, min, max, etc.)
    print("\nStatistical Summary:")
    print(sales_data.describe())

    # Check for missing values in each column
    print("\nMissing Values:")
    print(sales_data.isnull().sum())


def clean_sales_data(sales_data):
    """Handle missing values in sales column."""
    
    # Calculate average sales
    average_sales = sales_data["sales"].mean()
    
    # Fill missing values with average sales
    sales_data["sales"] = sales_data["sales"].fillna(average_sales)
    
    return sales_data


def add_analysis_columns(sales_data):
    """Add new columns for growth percentage and moving average."""
    
    # Calculate percentage growth compared to previous row
    sales_data["growth_percent"] = sales_data["sales"].pct_change() * 100
    
    # Calculate moving average over defined window
    sales_data["moving_average"] = (
        sales_data["sales"].rolling(window=MOVING_AVERAGE_MONTHS).mean()
    )
    
    return sales_data


def print_sales_statistics(sales_data):
    """Calculate and print statistical values using NumPy."""
    
    # Convert sales column to NumPy array
    sales_values = np.array(sales_data["sales"])

    print("\nNumPy Calculations:")
    
    # Calculate and print key statistics
    print("Mean:", np.mean(sales_values))
    print("Median:", np.median(sales_values))
    print("Standard Deviation:", np.std(sales_values))
    print("Max Sales:", np.max(sales_values))
    print("Min Sales:", np.min(sales_values))


def plot_sales_data(sales_data):
    """Plot sales data and moving average using Matplotlib."""
    
    # Create a new figure
    plt.figure()

    # Plot actual sales values
    plt.plot(sales_data["date"], sales_data["sales"], label="Actual Sales")

    # Plot moving average line
    plt.plot(
        sales_data["date"],
        sales_data["moving_average"],
        label=f"Moving Average ({MOVING_AVERAGE_MONTHS} months)",
    )

    # Label axes
    plt.xlabel("Date")
    plt.ylabel("Sales")

    # Add title and legend
    plt.title("Sales Data Analysis")
    plt.legend()

    # Rotate date labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plot
    plt.show()


def main():
    """Main function to execute the workflow."""
    
    # Load dataset
    sales_data = load_sales_data(DATA_FILE)

    # Display dataset overview
    print_dataset_overview(sales_data)

    # Clean data (handle missing values)
    sales_data = clean_sales_data(sales_data)

    # Add calculated columns
    sales_data = add_analysis_columns(sales_data)

    # Show updated dataset
    print("\nData with Growth and Moving Average Columns:")
    print(sales_data)

    # Print statistical analysis
    print_sales_statistics(sales_data)

    # Plot the results
    plot_sales_data(sales_data)


# Entry point of the program
if __name__ == "__main__":
    main()