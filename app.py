
import streamlit as st
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    confusion_matrix
)

st.set_page_config(
    page_title="Phishing Website Classification",
    page_icon="🔍",
    layout="wide"
)

st.title("Phishing Website Classification")
st.write("Classification of websites using five Machine Learning models.")

model_files = {
    "Logistic Regression": "model/logistic_regression.joblib",
    "Decision Tree": "model/decision_tree.joblib",
    "KNN": "model/knn.joblib",
    "Naive Bayes": "model/naive_bayes.joblib",
    "Support Vector Machine": "model/svm.joblib"
}

st.header("1. Upload Test Dataset")

uploaded_file = st.file_uploader(
    "Upload test_data.csv",
    type=["csv"]
)

if uploaded_file is not None:

    test_data = pd.read_csv(uploaded_file)

    st.success("Test dataset uploaded successfully.")

    st.write("Dataset shape:", test_data.shape)

    st.dataframe(test_data.head())

    if "target" not in test_data.columns:
        st.error("The uploaded CSV must contain a 'target' column.")
        st.stop()

    X_test = test_data.drop(columns=["target"])
    y_test = test_data["target"]

    st.header("2. Select Classification Model")

    selected_model = st.selectbox(
        "Choose a model:",
        list(model_files.keys())
    )

    model = joblib.load(model_files[selected_model])

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)

    st.header("3. Evaluation Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", f"{accuracy:.4f}")
        st.metric("Precision", f"{precision:.4f}")

    with col2:
        st.metric("AUC", f"{auc:.4f}")
        st.metric("Recall", f"{recall:.4f}")

    with col3:
        st.metric("F1 Score", f"{f1:.4f}")
        st.metric("MCC", f"{mcc:.4f}")

    st.header("4. Confusion Matrix")

    cm = confusion_matrix(y_test, y_pred)

    cm_df = pd.DataFrame(
        cm,
        index=["Actual 0", "Actual 1"],
        columns=["Predicted 0", "Predicted 1"]
    )

    st.dataframe(cm_df)

    st.write(f"Selected Model: **{selected_model}**")


    # --------------------------------------------------
    # Model Comparison - At the End
    # --------------------------------------------------

    st.header("5. Model Comparison")

    comparison_results = []

    for model_name, model_path in model_files.items():

        comparison_model = joblib.load(model_path)

        comparison_y_pred = comparison_model.predict(X_test)
        comparison_y_prob = comparison_model.predict_proba(X_test)[:, 1]

        comparison_results.append({
            "ML Model Name": model_name,
            "Accuracy": accuracy_score(
                y_test, comparison_y_pred
            ),
            "AUC": roc_auc_score(
                y_test, comparison_y_prob
            ),
            "Precision": precision_score(
                y_test, comparison_y_pred
            ),
            "Recall": recall_score(
                y_test, comparison_y_pred
            ),
            "F1": f1_score(
                y_test, comparison_y_pred
            ),
            "MCC": matthews_corrcoef(
                y_test, comparison_y_pred
            )
        })

    comparison_df = pd.DataFrame(comparison_results)

    st.dataframe(
        comparison_df.style.format({
            "Accuracy": "{:.4f}",
            "AUC": "{:.4f}",
            "Precision": "{:.4f}",
            "Recall": "{:.4f}",
            "F1": "{:.4f}",
            "MCC": "{:.4f}"
        }),
        use_container_width=True
    )
