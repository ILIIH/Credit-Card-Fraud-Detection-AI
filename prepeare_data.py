import pandas as pd

DATA_PATH = "data/creditcard.csv"

def load_and_refactor_data() : 
    df = pd.read_csv(DATA_PATH)
    print(df.head())