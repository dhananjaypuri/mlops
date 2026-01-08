# Logistic Regression - Disease Prediction Model

## Overview
This project implements a **Logistic Regression** model to predict whether a person has a disease based on health-related features. The model is trained using scikit-learn and evaluates performance using standard classification metrics.

## Dataset
- **File**: `logis_reg.csv`
- **Features**:
  - `Age`: Patient's age
  - `BMI`: Body Mass Index
  - `BloodPressure`: Blood pressure reading
  - `Smoker`: Smoking status (Yes/No)
- **Target**: `Has_Disease` (Binary: 0 = No Disease, 1 = Has Disease)

## Features
- Data preprocessing with label encoding for categorical variables
- Train-test split (80-20) with random state 42 for reproducibility
- Logistic Regression model implementation
- Comprehensive performance evaluation with multiple metrics
- Example prediction for a sample patient profile

## Requirements
```
pandas
scikit-learn
```

## Installation
Install required packages:
```bash
pip install pandas scikit-learn
```

## Usage
Run the script:
```bash
python logistic_reg.py
```

## Output Metrics
The model outputs the following evaluation metrics:
- **Accuracy**: Overall correctness of predictions
- **Precision**: True positives among all positive predictions
- **Recall**: True positives among all actual positives
- **F1-Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: True positives, false positives, false negatives, and true negatives

## Model Performance Example
```
Accuracy : [value]
Precision: [value]
Recall: [value]
F1-Score: [value]
Confusion Matrix: [[tn, fp], [fn, tp]]
```

## Sample Prediction
The model predicts the health status for a patient with:
- Age: 32
- BMI: 60
- Blood Pressure: 145
- Smoker: No (0)

Output: "User is fit and fine" or "User has disease"

## Project Structure
```
Logistic-Regression/
├── logistic_reg.py
├── logis_reg.csv
└── README.md
```

## Notes
- The `Smoker` feature is encoded using LabelEncoder (converting categorical values to numeric)
- Random state is set to 42 for reproducible results
- Test set size is 20% of the total data

## Author
MLOps Study Project
