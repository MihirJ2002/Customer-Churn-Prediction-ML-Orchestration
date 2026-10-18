
# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, RobustScaler, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer



def data_preprocessing(df):

    # Dropping Duplicate Customer Records
    df = df.drop_duplicates(subset=["customerID"]).copy()

    # Converting TotalCharges into Numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )

    # Dropping Unnecessary Columns
    df.drop(columns=["customerID"], inplace=True)

    # Encoding Target Variable
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Segregating Numerical and Categorical Columns
    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    numerical_data = X.select_dtypes(exclude="object").columns
    categorical_data = X.select_dtypes(include="object").columns

    # Using Train & Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Using Scaling Techniques
    numerical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", MinMaxScaler())
    ])

    # Encoding Categorical Features
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    # Combining Numerical and Categorical Pipelines
    preprocessor = ColumnTransformer([
        ("num", numerical_pipeline, numerical_data),
        ("cat", categorical_pipeline, categorical_data)
    ])

    # Applying Preprocessing
    X_train = preprocessor.fit_transform(X_train)  # Seen Data
    X_test = preprocessor.transform(X_test)        # Unseen Data

    return X_train, X_test, y_train, y_test
