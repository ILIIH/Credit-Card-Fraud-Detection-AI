import pandas as pd

DATA_PATH = "data/creditcard.csv"

def load_and_refactor_data() : 
    df = pd.read_csv(DATA_PATH)
    df_output = df[['Class']]
    df_features = df.drop(columns=['Class'])
    return df_output,df_features