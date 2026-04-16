def analyze_data(df):
    # Category-wise spending
    category_spending = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    # Monthly spending
    monthly_spending = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()

    return category_spending, monthly_spending