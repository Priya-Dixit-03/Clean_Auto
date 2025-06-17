import pandas as pd

def clean_data(df):
    df = df.copy()

    # Remove duplicates (entire row)
    df.drop_duplicates(inplace=True)

    # Trim whitespace from strings
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Fill missing values with 'N/A'
    df.fillna("N/A", inplace=True)

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Remove duplicate names (keep the first occurrence)
    if 'name' in df.columns:
        df = df.drop_duplicates(subset='name', keep='first')

    # Remove duplicate email ids (keep the first occurrence)
    if 'email' in df.columns:
        df = df.drop_duplicates(subset='email', keep='first')

    return df
