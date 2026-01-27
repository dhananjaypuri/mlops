# 🎯 Customer Segmentation using K-Means Clustering

Welcome to the **Customer Segmentation** project! This interactive machine learning project demonstrates how to segment customers into meaningful groups using **K-Means Clustering**.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Objective](#project-objective)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Key Concepts](#key-concepts)
- [Installation & Setup](#installation--setup)
- [Running the Code](#running-the-code)
- [Results & Interpretation](#results--interpretation)
- [Use Cases](#use-cases)

---

## 🔍 Overview

This project uses **unsupervised learning** to automatically categorize customers into three buyer groups based on their:
- **Age** 💰
- **Spending Pattern** 🛍️

No labels needed! The algorithm learns patterns directly from the data.

---

## 🎯 Project Objective

Divide customers into three distinct segments:

| Group | Description |
|-------|-------------|
| 🟢 **Small Buyer** | Low spending customers |
| 🟡 **Medium Buyer** | Moderate spending customers |
| 🔴 **Premium Buyer** | High-value customers |

---

## 📊 Dataset

The project includes **10 sample customers** with the following information:

```
Customer Name  | Age | Spending ($)
---|---|---
Alice Chen     | 28  | 150.50
Marcus Wright  | 45  | 1200.00
Sarah Jenkins  | 32  | 430.25
Leo Tanaka     | 21  | 85.00
Elena Rodriguez| 38  | 920.10
David Smith    | 54  | 55.40
Priya Sharma   | 29  | 310.00
Gary Wilson    | 61  | 15.20
Isabella Rossi | 35  | 740.00
James O'Connor | 42  | 510.75
```

---

## 🔧 How It Works

### Step 1: **Data Preparation** 📥
```
Load customer data (age, spending)
```

### Step 2: **Feature Scaling** ⚖️
```
Normalize the data using StandardScaler
(prevents larger values from dominating)
```

### Step 3: **Clustering** 🎲
```
Apply K-Means algorithm with 3 clusters
Groups similar customers together
```

### Step 4: **Prediction** 🔮
```
Test with new customer: Age=28, Spending=$800
Predict which group they belong to
```

### Step 5: **Evaluation** 📈
```
Calculate Silhouette Score
(measure of clustering quality: -1 to +1)
Higher score = better clustering
```

---

## 💡 Key Concepts

### K-Means Clustering
- **Unsupervised Learning**: No pre-labeled data needed
- **Centroid-based**: Creates clusters around central points
- **Iterative**: Refines groups until convergence

### Standardization
- Converts features to comparable scales
- Formula: `(value - mean) / standard_deviation`
- Ensures all features contribute equally

### Silhouette Score
- Ranges from -1 to 1
- **Close to 1**: Well-separated clusters
- **Close to 0**: Overlapping clusters
- **Close to -1**: Poorly clustered data

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pandas
- scikit-learn
- matplotlib

### Install Dependencies

```bash
pip install pandas scikit-learn matplotlib
```

---

## ▶️ Running the Code

### Option 1: Run the Script

```bash
python code.py
```

### Option 2: Interactive Mode

```python
# In Python/Jupyter:
exec(open('code.py').read())
```

### Expected Output

```
   customer_name  age   spending  Group
0      Alice Chen   28     150.50      0
1   Marcus Wright   45    1200.00      1
2   Sarah Jenkins   32     430.25      2
...

User is Medium Buyer
Silhouette Score: 0.6234...
```

---

## 📈 Results & Interpretation

### What Do The Results Tell Us?

1. **Customer Groups** 👥
   - Each customer is assigned to a group (0, 1, or 2)
   - Groups mapped to: Small Buyer, Medium Buyer, Premium Buyer

2. **New Customer Prediction** 🎯
   - A 28-year-old with $800 spending = **Medium Buyer**
   - Can predict future customers automatically!

3. **Silhouette Score** 📊
   - Indicates how well customers are grouped
   - Score > 0.5 is generally considered good

---

## 💼 Use Cases

### Real-World Applications

| Use Case | Benefit |
|----------|---------|
| **Marketing** | Targeted campaigns for each segment |
| **Pricing** | Different pricing tiers per group |
| **Customer Service** | Personalized support levels |
| **Inventory** | Stock products based on segment preferences |
| **Loyalty Programs** | Tailored rewards for each group |

---

## 🎓 Learning Outcomes

After completing this project, you'll understand:

✅ How K-Means clustering works  
✅ Why feature scaling matters  
✅ How to evaluate clustering quality  
✅ Real-world customer segmentation  
✅ How to make predictions on new data  

---

## 🔄 Try This!

**Experiment by changing:**

1. **Number of Clusters**: Change `n_clusters=3` to 2, 4, or 5
2. **New Customer**: Modify `[[28, 800]]` to test different ages/spending
3. **Random State**: Change `random_state=42` for different initial clusters

```python
# Example: Test with a 50-year-old with $5000 spending
result = model.predict(scaler.transform([[50, 5000]]))
print(cluster_map[result[0]])
```

---

## 📝 Notes

- This is a **demo project** with sample data
- Real datasets may require more preprocessing
- Consider feature engineering for better results
- Experiment with different K values (elbow method)

---

## 🤝 Contributing

Feel free to enhance this project:
- Add more customer data
- Implement elbow method
- Create visualizations
- Add more features (location, category preferences, etc.)

---

## 📚 Resources

- [Scikit-Learn K-Means Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Clustering in Machine Learning](https://en.wikipedia.org/wiki/Cluster_analysis)
- [Feature Scaling Guide](https://scikit-learn.org/stable/modules/preprocessing.html)

---

**Happy Clustering! 🚀**
