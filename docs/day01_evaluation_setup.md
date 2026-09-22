# Day 1 — Evaluation Code Setup

## Project

Malicious Botnet Traffic Detection Using Machine Learning

## Dataset

CTU-13

## Team Role

Member 4 — Evaluation, Results & Ablation

## Objective

The objective of Day 1 was to set up and validate the basic evaluation
pipeline required for evaluating machine learning model predictions.

## Environment

- Operating System: Windows
- Python: 3.13.13
- Virtual Environment: `.venv`
- Jupyter Notebook: Used for evaluation testing

## Libraries

- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Evaluation Components Implemented

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report
- Confusion Matrix

## Validation

A dummy binary-classification dataset was used to validate the evaluation
pipeline.

The dummy data was used only for testing and is not part of the final
CTU-13 experiment results.

## Reusable Evaluation Module

A reusable evaluation function was created in:

`src/evaluation.py`

The function accepts:

- `y_test` — actual test labels
- `y_pred` — model-predicted labels

and returns:

- Main evaluation metrics
- Classification report
- Confusion matrix

## Day 1 Result

The evaluation pipeline was successfully validated.

Status:

- Input validation: PASS
- Accuracy calculation: PASS
- Precision calculation: PASS
- Recall calculation: PASS
- F1-score calculation: PASS
- Classification report: PASS
- Confusion matrix: PASS
- Reusable evaluation module: PASS