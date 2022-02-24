import pandas as pd


def get_coordinates():
    data = pd.read_csv('data/coordinaten.csv')
    df = pd.DataFrame(data)
    df_records = df.to_records(index=False)
    df_list = list(df_records)
    return df_list
