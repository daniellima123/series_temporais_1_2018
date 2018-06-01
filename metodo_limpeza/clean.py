import pandas as pd
import os

def limpa_london(path):

    london_df = pd.read_csv(path, index_col='Date',
                                                        parse_dates=True).iloc[:,:-1]
    london_df = london_df.applymap(lambda x: None if(x in (-999, 9999)) else x)

    london_df['Maximo'] = london_df.filter(regex="^H").max(axis=1)


    return london_df



def limpa_PH(path):
    files = [x for x in os.listdir(path) if x.endswith(".CSV")]

    df_list = []
    for f in files:

        df = pd.read_csv(path+f, index_col='Date')
        df_list.append(df)
    df = pd.concat(df_list)
    df.index = pd.to_datetime(df.index, infer_datetime_format=True)

    return df
