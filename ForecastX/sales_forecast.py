from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


# File paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.csv"
CHART_FILE = BASE_DIR / "sales_chart.png"

MOVING_AVERAGE_MONTHS = 3


def load_sales_data(csv_path=DATA_FILE):
    """
    Load sales data from CSV file
    and calculate moving average.
    """

    sales_data = pd.read_csv(csv_path)

    required_columns = {"date", "sales"}

    missing_columns = required_columns - set(sales_data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required column(s): {', '.join(missing_columns)}"
        )

    # Convert columns
    sales_data["date"] = pd.to_datetime(sales_data["date"])
    sales_data["sales"] = pd.to_numeric(
        sales_data["sales"],
        errors="raise"
    )

    # Sort by date
    sales_data = sales_data.sort_values("date")

    # Calculate moving average
    sales_data["moving_average"] = (
        sales_data["sales"]
        .rolling(
            window=MOVING_AVERAGE_MONTHS,
            min_periods=1
        )
        .mean()
    )

    return sales_data


def plot_sales_data(
    sales_data,
    chart_path=CHART_FILE
):
    """
    Generate and save sales chart.
    """

    plt.figure(figsize=(10, 5))

    # Actual sales
    plt.plot(
        sales_data["date"],
        sales_data["sales"],
        marker="o",
        linewidth=2,
        label="Actual Sales"
    )

    # Moving average
    plt.plot(
        sales_data["date"],
        sales_data["moving_average"],
        marker="o",
        linewidth=2,
        linestyle="--",
        label=f"Moving Average ({MOVING_AVERAGE_MONTHS} months)"
    )

    plt.title("Sales Data Analysis")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.legend()

    plt.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(chart_path)

    plt.close()

    return chart_path


def main():
    """
    Main analysis workflow.
    """

    sales_data = load_sales_data()

    chart_path = plot_sales_data(sales_data)

    print(f"Chart saved successfully: {chart_path}")

    return chart_path


if __name__ == "__main__":
    main()
