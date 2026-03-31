# INFO-B211 — Assignment 7 (Matplotlib & Visual Analysis)

---

## **Answers to Visualization Questions**

---

### **1. What does the loan status distribution reveal about the dataset?**

| Loan Status   | Relative Frequency |
|---------------|--------------------|
| DEFAULT       | Higher             |
| NO DEFAULT    | Lower              |

**Loan status distribution**  
The horizontal bar chart shows that **DEFAULT** appears more often than **NO DEFAULT**.  
This suggests the dataset reflects a relatively high‑risk borrower population or is skewed toward loans with weaker credit profiles. The imbalance makes it especially important to examine other attributes (like loan grade) to understand why defaults are so common.

---

### **2. What relationship exists between customer income and loan amount?**

| Observation Type          | Insight                                      |
|---------------------------|----------------------------------------------|
| General trend             | Higher income → larger loans (loosely)       |
| Strength of relationship  | Weak to moderate                             |
| Notable exceptions        | Some low‑income borrowers get moderate loans |

**Income vs. loan amount**  
The scatter plot shows a **positive but loose relationship** between income and loan amount.  
Higher‑income borrowers tend to receive larger loans, but the pattern is not tightly clustered—there is a lot of spread. Some lower‑income borrowers still receive moderate loan amounts, which suggests that **loan size is influenced by more than income alone**, such as loan intent, loan grade, or employment duration.

---

### **3. How does default rate vary across loan grades?**

| Loan Grade | Default Rate Trend |
|------------|--------------------|
| A          | Lowest             |
| B          | Low–moderate       |
| C          | Moderate           |
| D          | High               |
| E          | Highest            |

**Default rate by loan grade**  
The line plot shows that **default rates increase as loan grade worsens**.  
Grade A loans have the lowest default rate, while grades D and E show significantly higher risk. This aligns with typical lending expectations—loan grade is a strong indicator of creditworthiness and repayment behavior. The visualization clearly communicates how risk escalates as you move from high‑quality to lower‑quality grades.

---

## **Overall Conclusions**

Across all three visualizations, several insights emerge:

- **Loan grade is the strongest predictor of default risk**, with lower grades showing sharply higher default rates.  
- **Income influences loan amount**, but not deterministically—borrowers with similar incomes can receive very different loan sizes.  
- **Defaults are relatively common** in this dataset, suggesting a risk‑heavy borrower pool or a dataset focused on higher‑risk lending scenarios.  

---

## **Project Purpose**

The purpose of this project is to demonstrate the use of Matplotlib and pandas for:  
  - cleaning and preprocessing real‑world financial data  
  - converting currency‑formatted values into numeric form  
  - generating clear, interpretable visualizations  
  - identifying trends in borrower behavior  
  - analyzing default risk across demographic and financial attributes  
  - comparing patterns across multiple datasets (Iris + Loan)  

The project emphasizes visual storytelling—using charts to uncover insights that would be difficult to detect from raw data alone.

---

## **Program Structure and Function Design**

The project is implemented using a modular, function‑based design. Each function performs one clear task and produces well‑defined visual output.

---

### **1. `save_and_show(filename)`**

**Purpose:**  
Save the current Matplotlib figure as a PNG and then display it.

**Inputs:**  
- `filename`: Name of the output image file.

**Behavior:**  
- Uses a consistent DPI and tight layout for all figures.  
- Avoids repeating save/show logic in every visualization function.

---

### **2. `iris_visualizations()`**

**Purpose:**  
Generate three visualizations for the Iris dataset.

**Visualizations:**  
- Sepal Length vs. Sepal Width scatter plot  
- Petal Length vs. Petal Width scatter plot  
- Mean Petal Length bar chart  

**Key details:**  
- Uses color‑grouped scatter plots to distinguish species.  
- Computes mean petal length per species and displays it as a bar chart.  
- Adds value labels above bars to make differences easy to read.

**Limitations:**  
- Uses only the built‑in Iris dataset.  
- No preprocessing or cleaning is required.

---

### **3. `loan_visualizations()`**

**Purpose:**  
Generate three visualizations for the loan dataset.

**Visualizations:**  
- Loan status distribution (horizontal bar chart with count labels)  
- Income vs. loan amount (scatter plot with cleaned numeric values)  
- Default rate by loan grade (line plot with labeled points)  

**Key details:**  
- Cleans `loan_amnt` by removing the `£` symbol, commas, and stray quotes, then converts it to numeric.  
- Converts `customer_income` to numeric and drops rows with missing or invalid values.  
- Computes default rates by loan grade using the proportion of rows where `Current_loan_status == "DEFAULT"`.  
- Adds value labels to bars, scatter points (loan amounts), and line markers (default rates).

**Limitations:**  
- Rows with invalid or missing numeric values are removed from some visualizations.  
- Missing loan grades are excluded from the default‑rate analysis.  
- The dataset may be skewed toward higher‑risk borrowers, so results may not generalize to all lending contexts.  
- Analysis is descriptive only—no predictive modeling is performed.

---

## **Limitations**

This project includes a few important constraints:

- **Data cleaning:** Currency‑formatted loan amounts required cleaning; rows that could not be converted to numeric were dropped.  
- **Missing values:** Records with missing loan grades or key numeric fields were excluded from some visualizations.  
- **Sample bias:** The dataset may not represent the full lending population, so conclusions apply only to this sample.  
- **Scope:** The Iris dataset is included to satisfy assignment requirements but is conceptually separate from the loan analysis.  

---
