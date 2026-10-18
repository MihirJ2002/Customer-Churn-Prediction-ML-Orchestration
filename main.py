
# Importing Necessary Libraries
from src.workflow import ml_workflow


def main():

    print("=" * 50)
    print("CUSTOMER CHURN PREDICTION")
    print("MACHINE LEARNING ORCHESTRATION")
    print("=" * 50)

    # Executing Complete ML Workflow
    results = ml_workflow()

    # Displaying Model Evaluation Results
    print("\nMODEL PERFORMANCE COMPARISON")

    for model_name, metrics in results.items():

        print(f"\nModel: {model_name}")

        print("Accuracy:", round(metrics["Accuracy"], 4))
        print("Precision:", round(metrics["Precision"], 4))
        print("Recall:", round(metrics["Recall"], 4))
        print("F1 Score:", round(metrics["F1 Score"], 4))
        print("ROC-AUC:", round(metrics["ROC-AUC"], 4))

    print("\nML Workflow Completed Successfully!")


if __name__ == "__main__":
    main()
