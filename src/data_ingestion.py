# import Data Mqanipulation libraries
import pandas as pd
import numpy as np



def data_loader():



    df = pd.read_csv(r"https://raw.githubusercontent.com/MihirJ2002/Customer-Churn-Prediction-ML-Orchestration/refs/heads/main/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    return df