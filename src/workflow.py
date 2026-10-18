

from prefect import flow, task
import mlflow
from src.data_ingestion import data_loader
from src.data_preprocessing import data_preprocessing
from src.model_training import model_training
from src.model_evaluation import model_evaluation

# MLflow Configuration
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Customer_Churn_Prediction")


# Step 1: Data Ingestion Task
@task(name="Data Ingestion", retries=2)
def ingestion_task():

    df = data_loader()

    return df


# Step 2: Data Preprocessing Task
@task(name="Data Preprocessing", retries=2)
def preprocessing_task(df):

    X_train, X_test, y_train, y_test = data_preprocessing(df)

    return X_train, X_test, y_train, y_test


# Step 3: Model Training Task
@task(name="Model Training", retries=2)
def training_task(X_train, y_train):

    models = model_training(X_train, y_train)

    return models



# Model Evaluation Task with MLflow Tracking
@task(name="Model Evaluation", retries=2)
def evaluation_task(models, X_test, y_test):

    results = {}

    # Evaluating All Models
    for name, model in models.items():

        print(f"\nEvaluating: {name}")

        # Starting MLflow Run
        with mlflow.start_run(run_name=name):

            # Model Evaluation
            metrics = model_evaluation(
                model,
                X_test,
                y_test
            )

            # Logging Model Information
            mlflow.set_tag("Model_Name", name)

            # Logging Evaluation Metrics
            mlflow.log_metric(
                "Accuracy", metrics["Accuracy"]
            )

            mlflow.log_metric(
                "Precision", metrics["Precision"]
            )

            mlflow.log_metric(
                "Recall", metrics["Recall"]
            )

            mlflow.log_metric(
                "F1_Score", metrics["F1 Score"]
            )

            mlflow.log_metric(
                "ROC_AUC", metrics["ROC-AUC"]
            )

            # Store Results
            results[name] = metrics

            print(f"{name} logged successfully in MLflow!")

    return results



# Step 5: ML Orchestration Workflow
@flow(name="Customer Churn ML Orchestration")
def ml_workflow():

    # Data Ingestion
    df = ingestion_task()

    # Data Preprocessing
    X_train, X_test, y_train, y_test = preprocessing_task(df)

    # Model Training
    models = training_task(X_train, y_train)

    # Model Evaluation
    results = evaluation_task(
        models,
        X_test,
        y_test
    )

    print("\nML Workflow Completed Successfully!")

    return results


# Execute Workflow
if __name__ == "__main__":
    ml_workflow()
