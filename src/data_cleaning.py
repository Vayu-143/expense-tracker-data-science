import pandas as pd

def clean_data():
    df = pd.read_csv("data/expenses.csv")

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Remove missing values
    df.dropna(inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    return df