from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = Path(__file__).with_name("data.csv")
CHART_FILE = Path(__file__).with_name("sales_chart.png")
MOVING_AVERAGE_MONTHS = 3


def load_sales_data(csv_path=DATA_FILE):
    """Load sales data and calculate a rolling moving average."""
    sales_data = pd.read_csv(csv_path)

    required_columns = {"date", "sales"}
    missing_columns = required_columns - set(sales_data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required column(s): {missing}")

    sales_data["date"] = pd.to_datetime(sales_data["date"])
    sales_data["sales"] = pd.to_numeric(sales_data["sales"], errors="raise")
    sales_data = sales_data.sort_values("date")
    sales_data["moving_average"] = sales_data["sales"].rolling(
        window=MOVING_AVERAGE_MONTHS,
        min_periods=1,
    ).mean()

    return sales_data


def plot_sales_data(sales_data, chart_path=CHART_FILE):
    """Plot sales data and moving average using Matplotlib."""
    plt.figure(figsize=(8, 5))

    plt.plot(
        sales_data["date"],
        sales_data["sales"],
        marker="o",
        label="Actual Sales",
    )

    plt.plot(
        sales_data["date"],
        sales_data["moving_average"],
        marker="o",
        label=f"Moving Average ({MOVING_AVERAGE_MONTHS} months)",
    )

    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Sales Data Analysis")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path


def main():
    sales_data = load_sales_data()
    chart_path = plot_sales_data(sales_data)
    print(f"Chart saved as {chart_path.name}")
    return chart_path


if __name__ == "__main__":
    main()
