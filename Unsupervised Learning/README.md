# Customer Segmentation Using K-Means Clustering

## Overview
This project implements unsupervised learning using K-Means clustering to segment customers into three distinct groups based on their age and spending patterns: **Small Buyers**, **Medium Buyers**, and **Premium Buyers**.

## Objective
The goal is to identify customer segments that can help with targeted marketing strategies, personalized offers, and customer relationship management.

## Dataset
The dataset contains information about 10 customers with the following features:
- **customer_name**: Name of the customer
- **age**: Age of the customer
- **spending**: Total spending amount (in currency units)

Sample customers include Alice Chen, Marcus Wright, Sarah Jenkins, and others with ages ranging from 21 to 61 years and spending amounts from $15.20 to $1,200.00.

## Methodology

### 1. **Data Preprocessing**
   - Features are standardized using `StandardScaler` to ensure equal weight for both age and spending in clustering

### 2. **K-Means Clustering**
   - Number of clusters: **3**
   - Random state: 42 (for reproducibility)
   - The algorithm partitions customers into 3 groups based on scaled features

### 3. **Cluster Labeling**
   - Clusters are mapped to business-meaningful labels based on average spending:
     - **Small Buyer**: Lowest average spending
     - **Medium Buyer**: Medium average spending
     - **Premium Buyer**: Highest average spending

### 4. **Model Evaluation**
   - **Silhouette Score** is calculated to evaluate the quality of clustering

## Key Features

- **Customer Grouping**: Automatically segments customers into three buyer categories
- **Prediction**: Can predict which segment a new customer belongs to (example: a 28-year-old with $800 spending)
- **Cluster Centers**: Displays average age and spending for each cluster
- **Performance Metrics**: Uses Silhouette Score to measure clustering quality

## Output

The script provides:
1. **DataFrame**: Customer list with assigned group labels
2. **Prediction Result**: Classification of a sample customer (28 years, $800 spending)
3. **Buyer Category**: Interpreted label (e.g., "User is Premium Buyer")
4. **Silhouette Score**: Quality metric for the clustering model

## Dependencies
```
pandas
scikit-learn
matplotlib
```

## Usage
Run the script using:
```bash
python code.py
```

## Applications
- Target marketing campaigns to specific customer segments
- Personalized pricing strategies for different buyer categories
- Customer retention programs tailored to each segment
- Inventory management based on customer spending patterns
