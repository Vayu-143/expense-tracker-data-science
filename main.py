from src.data_generator import generate_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import plot_category, plot_monthly

def main():
    # Step 1: Generate Data
    generate_data()

    # Step 2: Clean Data
    df = clean_data()

    # Step 3: Analyze
    category, monthly = analyze_data(df)

    # Step 4: Visualize
    plot_category(category)
    plot_monthly(monthly)

    # Step 5: Insights
    print("\n📊 BASIC INSIGHTS:")
    print("Top Category:", category.idxmax())
    print("Highest Spending Month:", monthly.idxmax())

    print("\n💡 ADVANCED INSIGHTS:")

    # Total spending
    total = df["Amount"].sum()
    print("Total Spending:", total)

    # Average spending
    avg = df["Amount"].mean()
    print("Average Spending:", round(avg, 2))

    # Highest transaction
    max_txn = df.loc[df["Amount"].idxmax()]
    print("\nHighest Transaction:")
    print(max_txn)

    # High spending detection
    high_spending = df[df["Amount"] > 3000]
    print("\nHigh Spending Transactions Count:", len(high_spending))


if __name__ == "__main__":
    main()