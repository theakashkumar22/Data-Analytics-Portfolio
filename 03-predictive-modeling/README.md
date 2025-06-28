# Superstore Sales Prediction Model

A comprehensive machine learning solution for predicting sales using the Superstore dataset with linear regression and Random Forest comparison.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Dataset](#dataset)
- [Usage](#usage)
- [Model Features](#model-features)
- [Results](#results)
- [Project Structure](#project-structure)

## 🎯 Overview

This project implements a predictive model to forecast sales using historical Superstore data. The solution includes comprehensive data preprocessing, feature engineering, model training, evaluation, and comparison between Linear Regression and Random Forest algorithms.


## ✨ Features

- **Complete Data Pipeline**: Automated data loading, cleaning, and preprocessing
- **Feature Engineering**: Creates temporal and categorical features from raw data
- **Model Training**: Linear Regression with scikit-learn
- **Model Comparison**: Compare Linear Regression vs Random Forest performance
- **Comprehensive Evaluation**: Multiple metrics and visualizations
- **Prediction Interface**: Easy-to-use prediction function for new data
- **Data Visualization**: Exploratory data analysis with plots

## 🛠 Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd superstore-sales-prediction
   ```

2. **Install required packages**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```

3. **Prepare your dataset**
   - Ensure your Superstore dataset is in CSV format
   - Place it in the project directory
   - Update the file path in the script

## 📊 Dataset

The model expects a Superstore dataset with the following columns:

| Column Name | Description |
|-------------|-------------|
| Row ID | Unique identifier for each row |
| Order ID | Unique identifier for each order |
| Order Date | Date when the order was placed |
| Ship Date | Date when the order was shipped |
| Ship Mode | Shipping method used |
| Customer ID | Unique identifier for each customer |
| Customer Name | Name of the customer |
| Segment | Customer segment (Consumer, Corporate, Home Office) |
| Country | Country where the order was placed |
| City | City where the order was placed |
| State | State where the order was placed |
| Postal Code | Postal code of the delivery address |
| Region | Geographic region |
| Product ID | Unique identifier for each product |
| Category | Product category |
| Sub-Category | Product sub-category |
| Product Name | Name of the product |
| **Sales** | Sales amount (target variable) |

## 🚀 Usage

### Quick Start

```python
from superstore_predictor import SuperstoreSalesPredictor, run_complete_analysis

# Run complete analysis pipeline
predictor, results, comparison = run_complete_analysis('your_superstore_file.csv')
```

### Step-by-Step Usage

```python
# 1. Initialize the predictor
predictor = SuperstoreSalesPredictor('superstore.csv')

# 2. Explore the data (optional)
predictor.explore_data()

# 3. Train the model
predictor.train_model()

# 4. Evaluate model performance
results = predictor.evaluate_model()

# 5. Compare with Random Forest
from superstore_predictor import compare_models
comparison_results = compare_models(predictor)

# 6. Make predictions on new data
prediction = predictor.predict_new_sales({
    'Order Year': 2023,
    'Order Month': 12,
    'Order Quarter': 4,
    'Order Day of Week': 1,
    'Shipping Days': 3,
    'Ship Mode': 'Standard Class',
    'Segment': 'Consumer',
    'Category': 'Technology',
    'Sub-Category': 'Phones',
    'Region': 'West'
})
```

### Making Predictions

To predict sales for new orders, use the `predict_new_sales()` method:

```python
new_order = {
    'Order Year': 2024,
    'Order Month': 6,
    'Order Quarter': 2,
    'Order Day of Week': 3,  # 0=Monday, 6=Sunday
    'Shipping Days': 2,
    'Ship Mode': 'Second Class',
    'Segment': 'Corporate',
    'Category': 'Furniture',
    'Sub-Category': 'Chairs',
    'Region': 'East'
}

predicted_sales = predictor.predict_new_sales(new_order)
print(f"Predicted Sales: ${predicted_sales:.2f}")
```

## 🔧 Model Features

The model uses the following engineered features:

### Temporal Features
- **Order Year**: Year when the order was placed
- **Order Month**: Month of the order (1-12)
- **Order Quarter**: Quarter of the year (1-4)
- **Order Day of Week**: Day of the week (0=Monday, 6=Sunday)
- **Shipping Days**: Number of days between order and ship date

### Categorical Features (Label Encoded)
- **Ship Mode**: Shipping method
- **Segment**: Customer segment
- **Category**: Product category
- **Sub-Category**: Product sub-category
- **Region**: Geographic region

## 📈 Results

The model provides comprehensive evaluation metrics:

### Performance Metrics
- **R² Score**: Coefficient of determination
- **RMSE**: Root Mean Squared Error
- **MAE**: Mean Absolute Error
- **MSE**: Mean Squared Error

### Visualizations
- **Actual vs Predicted**: Scatter plot showing prediction accuracy
- **Residuals Plot**: Shows prediction errors distribution
- **Feature Importance**: Bar chart of feature coefficients

### Model Comparison
Compare Linear Regression with Random Forest to determine the best approach for your data.

## 📁 Project Structure

```
predictive_model/
│
├── predictive_model.ipynb    # Main prediction model
├── README.md                  # Project documentation
├── superstore.csv           # Dataset
```

## 🔍 Example Output

```
==================================================
MODEL EVALUATION
==================================================
Performance Metrics:
Metric          Training     Testing     
----------------------------------------
R² Score        0.0047       0.0041      
RMSE            567.21       815.89      
MAE             253.20       300.77      
MSE             321724.82    665678.68

==================================================
MODEL COMPARISON
==================================================
Linear Regression - R²: 0.0041, RMSE: 815.89
Random Forest - R²: 0.0034, RMSE: 816.16

==================================================
MAKING PREDICTIONS
==================================================
Input data: {'Order Year': 2023, 'Order Month': 12, 'Order Quarter': 4, 'Order Day of Week': 1, 'Shipping Days': 3, 'Ship Mode': 'Standard Class', 'Segment': 'Consumer', 'Category': 'Technology', 'Sub-Category': 'Phones', 'Region': 'West'}
Predicted Sales: $277.20
```

## 🎯 Key Insights

- **Feature Importance**: The model identifies which factors most strongly influence sales
- **Seasonal Patterns**: Temporal features help capture seasonal sales variations
- **Category Impact**: Different product categories have varying sales patterns
- **Regional Differences**: Geographic regions show distinct sales characteristics

## 🔧 Customization

### Adding New Features
To add custom features, modify the `preprocess_data()` method:

```python
# Add custom features in the preprocessing step
df_processed['Custom_Feature'] = your_calculation
feature_columns.append('Custom_Feature')
```

### Changing Model Parameters
Modify the model initialization:

```python
# In train_model() method
self.model = LinearRegression(fit_intercept=True, normalize=False)
```
