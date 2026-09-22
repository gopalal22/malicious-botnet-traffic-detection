# Day 2 — Result Storage Format

## Project

Malicious Botnet Traffic Detection Using Machine Learning

## Team Role

Member 4 — Evaluation, Results & Ablation

## Objective

Define a consistent result-storage format for evaluating the five
machine learning models.

## Models

1. Decision Tree
2. Random Forest
3. AdaBoost
4. XGBoost
5. LightGBM

## Baseline Metrics

The baseline result table contains:

- Accuracy
- Precision
- Recall
- F1-score

## Storage Format

Results are stored in:

`results/metrics/baseline_results.csv`

## Schema

| Column | Description |
|---|---|
| model | Machine learning model name |
| accuracy | Accuracy score |
| precision | Precision score |
| recall | Recall score |
| f1_score | F1-score |

## Current Status

The result table currently contains the five model names with empty
metric fields.

No model performance values have been inserted yet because the actual
model evaluation has not been performed.

## Validation

- Result columns validated
- Five model entries validated
- CSV storage validated

Status: PASS