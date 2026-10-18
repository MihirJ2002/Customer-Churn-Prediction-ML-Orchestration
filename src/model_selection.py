
# Importing Necessary Libraries
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score


def select_best_model(models, X_train, y_train):

    results = {}

    # Stratified Cross Validation
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    # Comparing Models
    for name, model in models.items():

        scores = cross_val_score(
            model,
            X_train,
            y_train,
            cv=cv,
            scoring="roc_auc",
            n_jobs=-1
        )

        results[name] = scores.mean()

        print(f"{name}: {scores.mean():.4f}")

    # Selecting Best Model
    best_name = max(results, key=results.get)

    print("\nBest Model:", best_name)

    return best_name, results
