
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# ---------------------------------------------------------
# Helper function to save + show figures
# ---------------------------------------------------------
def save_and_show(filename):
    """Save the current Matplotlib figure, then show it."""
    plt.savefig(filename, dpi=300, bbox_inches="tight")  # Save high-quality PNG
    plt.show()  # Display the figure


# ---------------------------------------------------------
# IRIS VISUALIZATIONS
# ---------------------------------------------------------
def iris_visualizations():
    """Generate the 3 required Iris dataset visualizations."""

    iris = load_iris()  # Load built-in Iris dataset
    X = iris.data       # Feature matrix
    y = iris.target     # Species labels (0,1,2)
    species = iris.target_names  # Species names

    # ---------------------------------------------------------
    # Visualization 1: Sepal Length vs Sepal Width
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 6))  # Create new figure

    # Plot each species separately for color grouping
    for i in range(len(species)):
        plt.scatter(X[y == i, 0], X[y == i, 1],
                    label=species[i], alpha=0.7)

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Iris Dataset: Sepal Length vs Sepal Width")
    plt.legend()
    plt.grid(alpha=0.3)
    save_and_show("Iris_Sepal_Length_vs_Width_Scatter.png")

    # ---------------------------------------------------------
    # Visualization 2: Petal Length vs Petal Width
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 6))

    for i in range(len(species)):
        plt.scatter(X[y == i, 2], X[y == i, 3],
                    label=species[i], alpha=0.7)

    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Iris Dataset: Petal Length vs Petal Width")
    plt.legend()
    plt.grid(alpha=0.3)
    save_and_show("Iris_Petal_Length_vs_Width_Scatter.png")

    # ---------------------------------------------------------
    # Visualization 3: Mean Petal Length by Species
    # ---------------------------------------------------------
    mean_petal_length = [X[y == i, 2].mean() for i in range(len(species))]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(species, mean_petal_length,
                   color=["#6A5ACD", "#20B2AA", "#FF6347"])

    plt.xlabel("Species")
    plt.ylabel("Mean Petal Length (cm)")
    plt.title("Mean Petal Length by Iris Species")
    plt.grid(axis='y', alpha=0.3)

    # Add value labels above each bar
    for bar in bars:
        height = bar.get_height()  # Height = mean value
        plt.text(bar.get_x() + bar.get_width()/2,
                 height + 0.02,
                 f"{height:.2f}",
                 ha='center', fontsize=9)

    save_and_show("Iris_Mean_Petal_Length_Bar_Chart.png")


# ---------------------------------------------------------
# LOAN VISUALIZATIONS
# ---------------------------------------------------------
def loan_visualizations():
    """Generate the 3 required loan dataset visualizations."""

    df = pd.read_csv("LoansDataset.csv")  # Load dataset

    # ---------------------------------------------------------
    # CLEAN loan_amnt (currency → numeric)
    # ---------------------------------------------------------
    df['loan_amnt'] = (
        df['loan_amnt']
        .astype(str)                     # Ensure string type
        .str.replace("£", "", regex=False)  # Remove currency symbol
        .str.replace(",", "", regex=False)  # Remove commas
        .str.replace('"', "", regex=False)  # Remove stray quotes
        .str.strip()                      # Remove whitespace
    )

    df['loan_amnt'] = pd.to_numeric(df['loan_amnt'], errors='coerce')  # Convert to float
    df['customer_income'] = pd.to_numeric(df['customer_income'], errors='coerce')

    # ---------------------------------------------------------
    # Visualization 4: Loan Status Distribution
    # ---------------------------------------------------------
    plt.figure(figsize=(8, 6))

    status_counts = df['Current_loan_status'].value_counts()  # Count categories

    bars = plt.barh(status_counts.index, status_counts.values,
                    color='skyblue')  # Horizontal bar chart

    plt.title("Loan Status Distribution")
    plt.xlabel("Count")
    plt.ylabel("Loan Status")
    plt.grid(axis='x', alpha=0.3)

    # Add count labels to each bar
    for bar in bars:
        width = bar.get_width()  # Count value
        plt.text(width + 5, bar.get_y() + bar.get_height()/2,
                 str(width), va='center', fontsize=10)

    save_and_show("Loan_Status_Distribution.png")

    # ---------------------------------------------------------
    # Visualization 5: Income vs Loan Amount (Scatter Plot)
    # ---------------------------------------------------------
    df_clean = df.dropna(subset=['customer_income', 'loan_amnt'])  # Remove invalid rows

    plt.figure(figsize=(8, 6))

    plt.scatter(df_clean['customer_income'], df_clean['loan_amnt'],
                alpha=0.5, color='purple')  # Scatter plot

    plt.xlabel("Customer Income (£)")
    plt.ylabel("Loan Amount (£)")
    plt.title("Income vs Loan Amount")
    plt.grid(alpha=0.3)

    save_and_show("Income_vs_LoanAmount.png")

    # ---------------------------------------------------------
    # Visualization 6: Default Rate by Loan Grade
    # ---------------------------------------------------------
    df_grade = df.dropna(subset=['loan_grade'])  # Remove missing grades

    # Compute default rate per grade
    default_rates = df_grade.groupby('loan_grade')['Current_loan_status'].apply(
        lambda x: (x == 'DEFAULT').mean()  # Proportion of defaults
    )

    plt.figure(figsize=(8, 6))

    plt.plot(default_rates.index, default_rates.values,
             marker='o', color='darkred')  # Line plot

    plt.title("Default Rate by Loan Grade")
    plt.xlabel("Loan Grade")
    plt.ylabel("Default Rate (Proportion)")
    plt.grid(alpha=0.3)

    # Add value labels above each point
    for grade, rate in default_rates.items():
        plt.text(grade, rate + 0.01, f"{rate:.2f}",
                 ha='center', fontsize=10)

    save_and_show("DefaultRate_LineGraph.png")


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    """Run all visualizations."""
    iris_visualizations()   # Generate Iris plots
    loan_visualizations()   # Generate Loan dataset plots


if __name__ == "__main__":
    main()  # Execute program
