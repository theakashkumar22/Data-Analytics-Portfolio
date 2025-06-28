# 📊 SQL Analysis of Superstore Dataset

A comprehensive SQL-based analysis extracting actionable business insights from the Superstore dataset using advanced querying techniques and data visualization.

## 🎯 Objective

Demonstrate SQL proficiency through sales performance analysis, customer behavior insights, and product profitability assessment to drive strategic business decisions.

## 🛠️ Technology Stack

- **SQLite** + **Python** (sqlite3, Pandas)
- **Jupyter Notebook** for interactive analysis
- **Data Visualization** libraries for insights presentation

## 📈 Key Analysis Areas

1. **Regional Performance**: Sales and profit breakdown by geography
2. **Customer Intelligence**: High-value customer identification and segmentation
3. **Product Profitability**: Category and sub-category margin analysis
4. **Advanced Analytics**: Seasonal trends and shipping performance

## 🚀 Key Findings

- **West Region** leads in sales volume and profit contribution
- **Technology** category delivers highest profit margins (15.2% avg)
- **Phones** and **Chairs** dominate sub-category sales rankings
- **Corporate** customers show superior average order values

## 🔍 Sample Query
```sql
SELECT Region, ROUND(SUM(Sales), 2) as Total_Sales,
       ROUND(SUM(Profit), 2) as Total_Profit
FROM superstore 
GROUP BY Region ORDER BY Total_Sales DESC;
```

## 🚀 Quick Start

```bash
pip install pandas jupyter
jupyter notebook superstore_analysis.ipynb
```

## 📊 Deliverables

- Interactive SQL queries and analysis
- Comprehensive visualizations and dashboards
- Business intelligence insights and recommendations

---
*Professional SQL analysis demonstrating data analyst and business intelligence capabilities.*
