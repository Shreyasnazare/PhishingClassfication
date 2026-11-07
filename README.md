# Phishing Website Classification using Machine Learning

This project implements five machine learning classification models to classify websites as **phishing** or **legitimate** using the UCI Phishing Websites dataset.

A Streamlit application is also developed to upload test data, select a trained model, display evaluation metrics, show the confusion matrix, and compare the performance of all five models.

---

## 1. Problem Statement

The objective of this project is to classify websites as either **phishing** or **legitimate** using machine learning classification techniques.

Five different classification models are implemented using the same dataset. Their performance is evaluated and compared using the following six evaluation metrics:

- Accuracy
- AUC
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)

The trained models are saved and integrated into a Streamlit application for prediction and evaluation.

---

## 2. Dataset Description

### Dataset Used

| Property | Details |
|---|---|
| Dataset Name | UCI Phishing Websites |
| Source | UCI Machine Learning Repository |
| Dataset Link | https://archive.ics.uci.edu/dataset/327/phishing+websites |
| Number of Instances | 11,055 |
| Number of Input Features | 30 |
| Problem Type | Binary Classification |

The dataset contains 30 input features describing different characteristics of websites.

The input features contain encoded values such as `-1`, `0`, and `1`. The meaning of these values depends on the particular feature.

### Train-Test Split

An 80:20 train-test split was used for model training and evaluation.

| Dataset | Number of Instances | Percentage |
|---|---:|---:|
| Training Data | 8,844 | 80% |
| Test Data | 2,211 | 20% |
| **Total** | **11,055** | **100%** |

The data was split using:

| Parameter | Value |
|---|---|
| Train-Test Ratio | 80:20 |
| Random State | 42 |
| Stratification | Yes |

The held-out test dataset is saved as `test_data.csv`.

---

## 3. GitHub Repository Link

| Item | Details |
|---|---|
| GitHub Repository |  |

---

## 4. Models Used

Five classification models were implemented and evaluated on the same dataset.

| No. | Machine Learning Model |
|---:|---|
| 1 | Logistic Regression |
| 2 | Decision Tree Classifier |
| 3 | K-Nearest Neighbor (KNN) Classifier |
| 4 | Naive Bayes Classifier |
| 5 | Support Vector Machine (SVM) |

### Evaluation Metrics

Each model was evaluated using the six metrics required for the classification task.

| No. | Evaluation Metric |
|---:|---|
| 1 | Accuracy |
| 2 | AUC |
| 3 | Precision |
| 4 | Recall |
| 5 | F1 Score |
| 6 | Matthews Correlation Coefficient (MCC) |

---

## 5. Model Comparison

The performance of all five models on the held-out test dataset is shown below.

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9281 | 0.9785 | 0.9344 | 0.9010 | 0.9174 | 0.8542 |
| **Decision Tree** | **0.9697** | 0.9764 | **0.9760** | **0.9551** | **0.9654** | **0.9386** |
| KNN | 0.9471 | 0.9855 | 0.9499 | 0.9296 | 0.9397 | 0.8927 |
| Naive Bayes | 0.6160 | 0.9677 | 0.5359 | 0.9990 | 0.6975 | 0.4067 |
| Support Vector Machine | 0.9516 | **0.9877** | 0.9571 | 0.9327 | 0.9447 | 0.9019 |

---

## 6. Observations on Model Performance

| ML Model Name | Observation |
|---|---|
| **Logistic Regression** | Achieved 0.9281 accuracy and 0.9174 F1 score. It provides a good baseline performance but performs below Decision Tree, KNN and SVM on most metrics. |
| **Decision Tree** | Achieved the highest Accuracy, Precision, Recall, F1 Score and MCC. It provides the strongest overall performance on this dataset. |
| **KNN** | Achieved 0.9471 accuracy and 0.9397 F1 score. It performs better than Logistic Regression and Naive Bayes on most metrics. |
| **Naive Bayes** | Achieved a very high Recall of 0.9990, but its Precision is only 0.5359. This results in lower Accuracy, F1 and MCC compared with the other models. |
| **Support Vector Machine** | Achieved 0.9516 accuracy and the highest AUC of 0.9877. It provides strong overall performance but is below Decision Tree on most of the other metrics. |

---

## 7. Overall Winner

Based on the comparison of all six evaluation metrics, **Decision Tree** is selected as the overall winner.

| Metric | Best Performing Model | Score |
|---|---|---:|
| Accuracy | Decision Tree | **0.9697** |
| AUC | Support Vector Machine | **0.9877** |
| Precision | Decision Tree | **0.9760** |
| Recall | Decision Tree | **0.9551** |
| F1 Score | Decision Tree | **0.9654** |
| MCC | Decision Tree | **0.9386** |

### Winner: Decision Tree

Decision Tree achieves the best result in **five out of the six evaluation metrics**:

- Accuracy: **0.9697**
- Precision: **0.9760**
- Recall: **0.9551**
- F1 Score: **0.9654**
- MCC: **0.9386**

Support Vector Machine achieves the highest AUC of **0.9877**.

Therefore, based on the overall comparison across the six required metrics, **Decision Tree is the overall winner** for this dataset.

---

## 8. Streamlit Application

The project includes a Streamlit application implemented in `app.py`.

### Features

| Feature | Description |
|---|---|
| Dataset Upload | Upload the test dataset in CSV format |
| Model Selection | Select one of the five trained classification models |
| Evaluation Metrics | Display Accuracy, AUC, Precision, Recall, F1 Score and MCC |
| Confusion Matrix | Display the confusion matrix for the selected model |
| Model Comparison | Display the performance comparison of all five models |

The application loads the saved trained models from the `model` directory.

The uploaded test data is used for prediction and evaluation. The models are not retrained in the Streamlit application.

---

## 9. Project Structure

```text
project-folder/
│
├── app.py
├── requirements.txt
├── README.md
├── test_data.csv
├── 2026AJ05794.ipynb
│
└── model/
    ├── logistic_regression.joblib
    ├── decision_tree.joblib
    ├── knn.joblib
    ├── naive_bayes.joblib
    └── svm.joblib
