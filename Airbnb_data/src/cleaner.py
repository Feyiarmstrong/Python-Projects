import pandas as pd

def clean_airbnb_data(url: str) -> pd.DataFrame:

    df_raw = pd.read_csv(url)
    return df_raw.copy()