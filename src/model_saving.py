
# Importing Necessary Libraries
import os
import joblib


def save_model(model, preprocessor=None):

    # Creating Models Folder
    os.makedirs("models", exist_ok=True)

    # Saving Trained Model
    joblib.dump(
        model,
        "models/best_churn_model.pkl"
    )

    # Saving Fitted Preprocessor
    if preprocessor is not None:
        joblib.dump(
            preprocessor,
            "models/preprocessor.pkl"
        )

    print("Model Saved Successfully!")
