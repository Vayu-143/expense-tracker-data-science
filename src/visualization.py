import matplotlib.pyplot as plt
import os

# Ensure output folders exist
os.makedirs("outputs/charts", exist_ok=True)

def plot_category(category_spending):
    plt.figure()
    category_spending.plot(kind="bar")
    plt.title("Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("outputs/charts/category_spending.png")
    plt.close()

def plot_monthly(monthly_spending):
    plt.figure()
    monthly_spending.plot(marker='o')
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("outputs/charts/monthly_spending.png")
    plt.close()