-- Create table for Superstore data (run once via Python or SQLite client)
CREATE TABLE superstore (
    Row_ID INTEGER,
    Order_ID TEXT,
    Order_Date TEXT,
    Ship_Date TEXT,
    Ship_Mode TEXT,
    Customer_ID TEXT,
    Customer_Name TEXT,
    Segment TEXT,
    Country TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Region TEXT,
    Product_ID TEXT,
    Category TEXT,
    Sub_Category TEXT,
    Product_Name TEXT,
    Sales REAL,
    Quantity INTEGER,
    Discount REAL,
    Profit REAL
);

-- Query 1: Total sales and profit by region
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS TotalSales,
    ROUND(SUM(Profit), 2) AS TotalProfit
FROM superstore
GROUP BY Region
ORDER BY TotalSales DESC;

-- Query 2: Top 5 customers by sales
SELECT 
    Customer_ID,
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS OrderCount,
    ROUND(SUM(Sales), 2) AS TotalSales
FROM superstore
GROUP BY Customer_ID, Customer_Name
ORDER BY TotalSales DESC
LIMIT 5;

-- Query 3: Profitability by product category
SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS TotalSales,
    ROUND(SUM(Profit), 2) AS TotalProfit,
    ROUND(AVG(Profit / Sales * 100), 2) AS ProfitMargin
FROM superstore
GROUP BY Category
ORDER BY ProfitMargin DESC;

-- Query 4: Bonus - Top sub-categories by sales
SELECT 
    Sub_Category,
    ROUND(SUM(Sales), 2) AS TotalSales
FROM superstore
GROUP BY Sub_Category
ORDER BY TotalSales DESC
LIMIT 5;
