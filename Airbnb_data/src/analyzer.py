import pandas as pd

def load_enriched_data(file_path: str = "data/clean_enriched.csv") -> pd.DataFrame:
    """
    Load the enriched Airbnb dataset for analysis.

    Parameters:
        file_path (str): Path to the enriched CSV file.

    Returns:
        pd.DataFrame: Enriched Airbnb DataFrame with all derived columns.
    """
    df_enriched = pd.read_csv(file_path)
    return df_enriched