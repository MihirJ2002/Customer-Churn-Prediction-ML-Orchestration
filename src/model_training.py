
# Importing Necessary Libraries
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def model_training(X_train, y_train):

    # Creating Logistic Regression Model
    lr = LogisticRegression(
        max_iter=1000,
        random_state=42
    )

    lr.fit(X_train, y_train)

    # Creating Random Forest Classifier Model
    rf = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    rf.fit(X_train, y_train)

    # Creating XGBoost Classifier Model
    xgb = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        eval_metric="logloss",
        random_state=42
    )

    xgb.fit(X_train, y_train)

    # Storing Trained Models
    models = {
        "Logistic Regression": lr,
        "Random Forest": rf,
        "XGBoost": xgb
    }

    print("All Models Trained Successfully!")

    return models
