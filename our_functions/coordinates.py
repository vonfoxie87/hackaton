import pandas as pd

def get_coordinates():
    data = pd.read_csv('../data/coordinaten.csv')
    # maak dataframe
    df = pd.DataFrame(data) 
    # maak losse rijen
    df_records = df.to_records(index=False)
    # maak de list
    df_list = list(df_records)

    return df_list
