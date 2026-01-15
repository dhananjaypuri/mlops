# Finetuned Student Result Calculator

A machine learning project that predicts student exam results using linear regression and logistic regression models.

## Overview

This project builds two predictive models to analyze and forecast student performance based on study habits and previous academic records:

1. **Linear Regression Model**: Predicts the final exam marks
2. **Logistic Regression Model**: Predicts whether a student will pass or fail the exam

## Features

The models use the following input features to make predictions:
- **Study_Hours_Per_Day**: Number of hours studied per day
- **Previous_Exam_Marks**: Marks obtained in the previous exam

## Dataset

The project uses `student_data.csv` which contains comprehensive student data including:
- Study hours per day
- Attendance percentage
- Previous exam marks
- Sleep hours
- Tuition status
- Internet access
- Extra-curricular activities
- Stress level
- Final marks (target variable)

## Models

### Model 1: Linear Regression
- **Purpose**: Predicts the actual final exam marks
- **Features**: Study_Hours_Per_Day, Previous_Exam_Marks
- **Output**: Numerical score for final marks

### Model 2: Logistic Regression
- **Purpose**: Predicts pass/fail status
- **Features**: Study_Hours_Per_Day, Previous_Exam_Marks
- **Pass Criteria**: Final marks >= 33
- **Custom Threshold**: 0.56 (probability threshold for pass prediction)

## How It Works

1. **Data Loading**: Reads student data from CSV file
2. **Data Preprocessing**: Creates a binary 'Result' column (Pass=1, Fail=0)
3. **Train-Test Split**: Splits data into 80% training and 20% testing sets (random_state=42)
4. **Model Training**: Trains both regression and classification models
5. **Prediction**: Makes predictions on new student data using a custom probability threshold

## Usage Example

```python
# Input: [Study Hours Per Day, Previous Exam Marks]
new_input = [[3.9, 40]]

# Predict marks
predicted_marks = reg_model.predict(new_input)
print(predicted_marks)

# Predict result with custom threshold
pass_proba = clf_model.predict_proba(new_input)[0][1]
final_result = 'Pass' if pass_proba >= 0.56 else 'Fail'
print(final_result)
```

## Requirements

- pandas
- scikit-learn
- numpy

## Installation

```bash
pip install pandas scikit-learn numpy
```

## Running the Script

```bash
python finetune.py
```

## Output

The script outputs:
1. Predicted final marks for the sample input
2. Pass/Fail prediction using standard logistic regression
3. Pass probability scores
4. Final result based on custom threshold (0.56)

## Key Insights

- The model uses a custom probability threshold (0.56) instead of the default (0.50) for more accurate pass/fail predictions
- Training data is split 80-20 to ensure model validation
- Both study hours and previous performance are strong indicators of final exam results
