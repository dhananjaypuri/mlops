# Student Result Calculator

## Project Overview
This project uses machine learning models to predict student academic performance based on study habits and previous exam scores. It implements two predictive models: one for predicting final marks and another for predicting pass/fail outcomes.

## Objectives
1. **Predict Final Marks**: Build a Linear Regression model to estimate a student's final exam marks
2. **Predict Pass/Fail Status**: Build a Logistic Regression model to classify students as Pass (≥33 marks) or Fail (<33 marks)
3. **Feature Analysis**: Understand the relationship between study hours, previous exam performance, and final results

## Dataset

### File: `student_marks_project1.csv`

### Features
- **Study_Hours_Per_Day**: Daily study hours (numeric)
- **Previous_Exam_Marks**: Marks obtained in previous exam (numeric)
- **Final_Marks**: Marks obtained in final exam (numeric)

### Target Variables
- **Final_Marks**: Used for regression model (predicting actual marks)
- **Result**: Binary classification (Pass=1 if Final_Marks ≥ 33, Fail=0 if Final_Marks < 33)

## Models & Methodology

### Model 1: Linear Regression
- **Purpose**: Predict the exact final exam marks
- **Input Features**: Study_Hours_Per_Day, Previous_Exam_Marks
- **Output**: Predicted final marks (continuous value)
- **Train-Test Split**: 80-20 split with random state = 42

### Model 2: Logistic Regression
- **Purpose**: Classify students as Pass or Fail
- **Input Features**: Study_Hours_Per_Day, Previous_Exam_Marks
- **Output**: Binary prediction (1 for Pass, 0 for Fail)
- **Pass Threshold**: Final marks ≥ 33
- **Train-Test Split**: 80-20 split with random state = 42

## Installation & Requirements

### Dependencies
```
pandas
scikit-learn
numpy
```

### Install Dependencies
```bash
pip install pandas scikit-learn numpy
```

## Usage

### Running the Script
```bash
python code.py
```

### What the Script Does
1. Loads the CSV dataset
2. Displays first few rows of data (`df.head()`)
3. Checks for missing values (`df.isnull().sum()`)
4. Creates binary Result column (Pass/Fail based on 33 mark threshold)
5. Trains Linear Regression model for marks prediction
6. Trains Logistic Regression model for pass/fail prediction
7. Makes sample predictions for input: `[[1, 50]]` (1 hour study, 50 previous marks)

### Sample Output
The script outputs two predictions for a student with:
- Study Hours Per Day: 1
- Previous Exam Marks: 50

Output includes:
- Predicted Final Marks (from Linear Regression)
- Predicted Result (from Logistic Regression)

## Key Insights

- **Pass Criterion**: A student needs at least 33 marks to pass
- **Predictor Variables**: Study hours and previous exam performance are strong indicators of final exam results
- **Data Validation**: The code checks for null values before model training

## Code Structure

| Component | Description |
|-----------|-------------|
| Data Loading | Reads CSV file using pandas |
| Data Exploration | Displays head and null value statistics |
| Feature Engineering | Creates binary 'Result' column based on threshold |
| Model 1 Training | Trains Linear Regression on marks prediction |
| Model 2 Training | Trains Logistic Regression on pass/fail classification |
| Predictions | Makes sample predictions with new inputs |

## Future Enhancements

1. Add model evaluation metrics (MSE, R², precision, recall, F1-score)
2. Perform feature scaling/normalization
3. Implement cross-validation
4. Add hyperparameter tuning
5. Create visualizations (scatter plots, correlation matrices)
6. Handle missing values more robustly
7. Add data preprocessing pipeline
8. Generate detailed performance reports

## Notes

- The model uses a fixed random state (42) for reproducibility
- No data preprocessing or feature scaling is applied in the current version
- Missing values are checked but not handled (assumes clean data)
- All semicolons at end of statements are optional in Python

## Author
Student Result Calculator Project

## License
Open Source
