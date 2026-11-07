# Phishing Website Classification using Machine Learning

This project implements five machine learning classification models to classify websites as **phishing** or **legitimate** using the UCI Phishing Websites dataset.

A Streamlit application is also developed to upload test data, select a trained model, display evaluation metrics, show the confusion matrix, compare the performance of all five models, and identify the overall winning model.

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

### Duplicate Records

Duplicate feature records were checked and removed before model training.

| Item | Details |
|---|---:|
| Original Instances | 11,055 |
| Duplicate Feature Rows | 5,270 |
| Duplicate Records Removed | 5,270 |

After removing duplicate feature records, the remaining unique records were used for the train-test split.

### Train-Test Split

An 80:20 train-test split was applied after duplicate record removal.

| Dataset | Percentage |
|---|---:|
| Training Data | 80% |
| Test Data | 20% |

The data was split using:

| Parameter | Value |
|---|---|
| Train-Test Ratio | 80:20 |
| Random State | 42 |
| Stratification | Yes |

The held-out test dataset is saved as `test_data.csv`.

---

## 3. GitHub Repository and Streamlit Application

| Item | Details |
|---|---|
| GitHub Repository | https://github.com/Shreyasnazare/PhishingClassfication |
| Streamlit Application | https://phishingclassfication-2026aj05794.streamlit.app/ |

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

Each model was evaluated using the six required evaluation metrics.

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
| Logistic Regression | 0.9343 | 0.9831 | 0.9468 | 0.9246 | 0.9356 | 0.8688 |
| Decision Tree | 0.9386 | 0.9388 | 0.9473 | 0.9330 | 0.9401 | 0.8773 |
| KNN | 0.9421 | 0.9829 | 0.9446 | 0.9430 | 0.9438 | 0.8841 |
| Naive Bayes | 0.6586 | 0.9742 | 0.6018 | 1.0000 | 0.7514 | 0.4211 |
| **Support Vector Machine** | **0.9525** | **0.9897** | **0.9705** | **0.9363** | **0.9531** | **0.9055** |

---

## 6. Overall Winner

Based on the highest average score across all six evaluation metrics, **Support Vector Machine (SVM)** is selected as the overall winner.

| Item | Result |
|---|---|
| **Overall Winner** | **Support Vector Machine (SVM)** |
| **Overall Score** | **0.9513** |

The overall winner is selected based on the highest average score across:

- Accuracy
- AUC
- Precision
- Recall
- F1 Score
- MCC

### Winning Model Performance

| Metric | Support Vector Machine Score |
|---|---:|
| Accuracy | **0.9525** |
| AUC | **0.9897** |
| Precision | **0.9705** |
| Recall | **0.9363** |
| F1 Score | **0.9531** |
| MCC | **0.9055** |

Support Vector Machine achieves the highest overall average score of **0.9513** and is therefore the **overall winner** for this dataset.

---

## 7. Observations on Model Performance

| ML Model Name | Observation |
|---|---|
| **Logistic Regression** | Achieved 0.9343 accuracy and 0.9356 F1 score. It provides good overall performance and serves as a strong baseline model. |
| **Decision Tree** | Achieved 0.9386 accuracy and 0.9401 F1 score. It provides consistent performance across the evaluation metrics but has a lower AUC compared with the other strong-performing models. |
| **KNN** | Achieved 0.9421 accuracy and 0.9438 F1 score. It provides strong overall performance and performs better than Logistic Regression and Decision Tree on several metrics. |
| **Naive Bayes** | Achieved a Recall of 1.0000, meaning it correctly identifies all positive instances. However, its Accuracy, Precision, F1 Score and MCC are substantially lower than the other models. |
| **Support Vector Machine** | Achieved the highest Accuracy (0.9525), AUC (0.9897), Precision (0.9705), F1 Score (0.9531) and MCC (0.9055). It provides the strongest overall performance and is selected as the overall winner. |

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
| Overall Winner | Display the model with the highest average score across the six evaluation metrics |

The application loads the saved trained models from the `model` directory.

The uploaded test data is used for prediction and evaluation. The models are not retrained in the Streamlit application.

---

## 9. Requirements

The required Python libraries are listed in `requirements.txt`.

### Install Required Libraries

Run the following command from the project directory:

```bash
pip install -r requirements.txt
