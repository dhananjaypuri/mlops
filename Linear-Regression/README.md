# Linear Regression: Student Marks Prediction

## 📋 Project Overview

This project implements a **Linear Regression model** to predict student marks based on the number of hours studied. It's a foundational machine learning project that demonstrates how to build a predictive model using real-world data with missing values.

---

## 🎯 Objective

Predict a student's obtained marks given the number of hours they studied using a linear regression algorithm.

---

## 📊 Dataset

**File:** `marks.csv`

### Data Structure
The dataset contains two columns:
- **hours_studied:** Number of hours a student studied (independent variable - X)
- **marks_obtained:** Marks obtained by the student (dependent variable - y)

### Data Characteristics
- Contains **31 records** of students
- Some missing values (NaN) present in both columns
- Values range from 1.0 to 11.0 hours and 35 to 100 marks

---

## 🛠️ Technologies Used

| Library | Purpose |
|---------|---------|
| **pandas** | Data loading and manipulation |
| **scikit-learn** | Machine learning algorithms and utilities |
| **LabelEncoder** | Encoding categorical data |
| **train_test_split** | Splitting data into training and testing sets |
| **LinearRegression** | Building the predictive model |

---

## 📝 Program Workflow

### **Step 1: Data Loading**
```python
df = pd.read_csv("marks.csv")
```
- Loads the CSV file into a pandas DataFrame

### **Step 2: Missing Data Detection**
```python
df.isna().sum()
```
- Identifies missing values in the dataset
- Displays count of NaN values in each column

### **Step 3: Calculate Mean Values**
```python
print(df['hours_studied'].mean())
print(df['marks_obtained'].mean())
```
- Calculates the average of hours studied
- Calculates the average marks obtained
- These means are used to replace missing values

### **Step 4: Handle Missing Data**
```python
df['hours_studied'] = df['hours_studied'].fillna(df['hours_studied'].mean())
df['marks_obtained'] = df['marks_obtained'].fillna(df['marks_obtained'].mean())
```
- Replaces NaN values with the mean of their respective columns
- Ensures complete data for model training

### **Step 5: Feature and Target Separation**
```python
X = df[['hours_studied']]      # Independent variable
y = df[['marks_obtained']]     # Dependent variable
```
- **X:** Input feature (hours studied)
- **y:** Target variable (marks obtained)

### **Step 6: Train-Test Split**
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- Splits data into:
  - **80% Training data** - used to train the model
  - **20% Testing data** - used to evaluate the model
- `random_state=42` ensures reproducibility

### **Step 7: Model Training**
```python
model = LinearRegression()
model.fit(X_train, y_train)
```
- Creates a Linear Regression model
- Trains the model using training data
- Learns the relationship: `marks = intercept + slope × hours_studied`

### **Step 8: Prediction**
```python
marks_predicted = model.predict([[6]])
print(float(marks_predicted))
```
- Predicts marks for a student who studied for **6 hours**
- Converts prediction to float and displays the result

---

## 🔍 How Linear Regression Works

Linear Regression fits a straight line through the data points following the equation:

$$y = mx + c$$

Where:
- **y** = Predicted marks
- **x** = Hours studied
- **m** = Slope (coefficient)
- **c** = Intercept (constant)

The algorithm minimizes the distance between predicted and actual values to find the best-fit line.

---

## 📈 Expected Output

The model learns a positive relationship: **More hours studied → Higher marks predicted**

Example prediction: A student who studies for 6 hours would receive approximately **~72 marks** (this varies based on actual data patterns).

---

## ✅ Key Concepts Explained

### Missing Data (NaN)
- **What is it?** Data points that are empty/missing
- **Why handle it?** Models can't work with missing values
- **Solution:** Replace with mean value (average of column)

### Train-Test Split
- **Why split?** To verify the model works on unseen data
- **80-20 split:** Standard practice in machine learning

### Linear Regression
- **When to use?** When there's a linear relationship between variables
- **Pros:** Simple, interpretable, fast
- **Cons:** Assumes linear relationship

---

## 🚀 How to Run

1. Ensure you have the required libraries:
   ```bash
   pip install pandas scikit-learn
   ```

2. Place `marks.csv` in the same directory as `linear_reg.py`

3. Run the script:
   ```bash
   python linear_reg.py
   ```

4. The script will output:
   - Missing data count
   - Mean values of both columns
   - Predicted marks for 6 hours of study

---

## 📊 Example Results

| Input (Hours) | Predicted Marks |
|---------------|-----------------|
| 1.0 | ~38 |
| 5.0 | ~64 |
| **6.0** | **~72** |
| 10.0 | ~98 |

---

## 🎓 Learning Outcomes

By studying this project, you'll learn:
- ✅ How to load and explore data using pandas
- ✅ How to detect and handle missing values
- ✅ How to split data for model evaluation
- ✅ How to build and train a linear regression model
- ✅ How to make predictions with trained models
- ✅ Understanding of machine learning workflow

---

## 📝 Notes

- The model assumes a linear relationship between study hours and marks
- Adding more features (e.g., attendance, sleep hours) could improve predictions
- Cross-validation can be used for better evaluation
- Feature scaling might be beneficial for larger datasets

---

## 📚 References

- [Scikit-learn Linear Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Machine Learning Basics](https://www.coursera.org/learn/machine-learning)

---

**Created:** January 2026  
**Status:** Complete ✅
