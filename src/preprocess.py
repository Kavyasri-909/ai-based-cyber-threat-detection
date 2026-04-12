import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    df = df.dropna()

    le = LabelEncoder()

    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    return df