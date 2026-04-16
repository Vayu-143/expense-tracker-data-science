import pandas as pd
import numpy as np
import os

def generate_data():
    np.random.seed(42)

    # Ensure folder exists
    os.makedirs("data", exist_ok=True)

    dates = pd.date_range(start="2024-01-01", periods=120)

    categories = ["Food", "Travel", "Shopping", "Bills", "Entertainment"]
    payment_methods = ["Cash", "Card", "UPI"]

    data = {
        "Date": np.random.choice(dates, 300),
        "Category": np.random.choice(categories, 300),
        "Amount": np.random.randint(50, 5000, 300),
        "Payment_Method": np.random.choice(payment_methods, 300)
    }

    df = pd.DataFrame(data)

    df.to_csv("data/expenses.csv", index=False)

    print("✅ Data generated successfully!")