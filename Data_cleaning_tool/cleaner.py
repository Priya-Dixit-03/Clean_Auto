import pandas as pd

def clean_data(df):
    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Trim whitespace from strings
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Fill missing values with 'N/A'
    df.fillna("N/A", inplace=True)

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    return df
