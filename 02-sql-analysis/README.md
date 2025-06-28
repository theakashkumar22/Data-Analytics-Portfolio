# Superstore Dataset SQL Analysis

This project demonstrates SQL proficiency by analyzing the Superstore dataset to uncover actionable business insights into sales, customer behavior, and product profitability.

## Project Objective
The goal is to extract meaningful insights from the Superstore dataset using SQL queries executed via SQLite and Python. The analysis focuses on regional performance, customer purchasing patterns, and product profitability to inform business strategies.

## Dataset
The Superstore dataset is a sample retail dataset containing sales transactions with fields such as:
- `Region`, `Sales`, `Profit`, `Customer_ID`, `Customer_Name`
- `Category`, `Sub_Category`, `Order_ID`, `Order_Date`

*Note*: Assumes a standard Superstore schema. Adjust queries if your dataset varies.

## Tools and Technologies
- **SQLite**: Lightweight database for executing SQL queries.
- **Python**: Uses `sqlite3` for database connectivity and `pandas` for data manipulation.
- **Jupyter Notebook**: Interactive environment for running and visualizing queries.

## Setup Instructions
1. **Install Dependencies**:
   Install required Python libraries:
   ```bash
   pip install pandas
   ```

2. **Launch Jupyter Notebook**:
   Start Jupyter to run the analysis:
   ```bash
   jupyter notebook
   ```

3. **Load Dataset**:
   - Place the Superstore dataset (e.g., `superstore.csv`) in your project directory.
   - Use the provided Python script to load the CSV into an SQLite database.

## Sample Setup Code
Below is a Python script to load the dataset into SQLite and run queries in Jupyter Notebook:

```python
import pandas as pd
import sqlite3

# Load CSV into DataFrame
df = pd.read_csv('superstore.csv')

# Create SQLite connection and load data
conn = sqlite3.connect('superstore.db')
df.to_sql('superstore', conn, if_exists='replace', index=False)

# Example query
query = "SELECT Region, SUM(Sales) as Total_Sales FROM superstore GROUP BY Region ORDER BY Total_Sales DESC;"
result = pd.read_sql_query(query, conn)
print(result)

# Close connection
conn.close()
```

## SQL Queries and Objectives
The analysis addresses the following key questions:

1. **Sales by Region**:
   - Query: Identify top-performing regions by total sales and profit.
   - Example:
     ```sql
     SELECT Region, SUM(Sales) as Total_Sales, SUM(Profit) as Total_Profit
     FROM superstore
     GROUP BY Region
     ORDER BY Total_Sales DESC;
     ```

2. **Top Customers**:
   - Query: Highlight customers with the highest sales and order frequency.
   - Example:
     ```sql
     SELECT Customer_Name, SUM(Sales) as Total_Sales, COUNT(DISTINCT Order_ID) as Order_Count
     FROM superstore
     GROUP BY Customer_Name
     ORDER BY Total_Sales DESC
     LIMIT 10;
     ```

3. **Profit Margin by Category**:
   - Query: Calculate profit margins by product category to assess profitability.
   - Example:
     ```sql
     SELECT Category, SUM(Profit) / SUM(Sales) * 100 as Profit_Margin
     FROM superstore
     GROUP BY Category
     ORDER BY Profit_Margin DESC;
     ```

4. **Top Sub-Categories**:
   - Query: List sub-categories with the highest sales.
   - Example:
     ```sql
     SELECT Sub_Category, SUM(Sales) as Total_Sales
     FROM superstore
     GROUP BY Sub_Category
     ORDER BY Total_Sales DESC
     LIMIT 5;
     ```

## Key Findings
- **Regional Performance**: The West region leads in both sales and profit, indicating strong market presence.
- **Customer Insights**: Top customers contribute significantly to revenue, with a few accounting for high order volumes.
- **Profitability**: The Technology category has the highest profit margin, making it a key focus for inventory.
- **Top Products**: Phones and Chairs are the top-selling sub-categories, driving significant sales volume.

## How to Run
1. Clone or download this repository.
2. Ensure the Superstore dataset (`superstore.csv`) is in the project directory.
3. Install dependencies and launch Jupyter Notebook (see Setup Instructions).
4. Run the Python script to load the dataset into SQLite.
5. Execute the SQL queries in Jupyter Notebook to replicate the analysis.

## Future Enhancements
- Add time-based analysis (e.g., sales trends by month or year).
- Incorporate visualizations using Matplotlib or Seaborn for better insights.
- Expand analysis to include discounts and their impact on profitability.
