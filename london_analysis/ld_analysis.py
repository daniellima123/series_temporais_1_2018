import pandas as pd
import matplotlib.pyplot as plt
import os

def criador_de_serie(df):
    valor = []
    for i in range(0, df.shape[0]):
        aux = df.iloc[i, 2:].max()
        valor.append(aux)
    serie = pd.DataFrame({'Station ID':df['Station ID'],
                          'Pollutant': df['Pollutant'],
                          'Valor': valor}, index=df.index)

    return serie
if __name__ == '__main__':


    london_df = pd.read_csv('Matter2013-London.csv', index_col='Date').iloc[:,:-1]
    london_df = london_df.applymap(lambda x: None if(x in (-999, 9999)) else x)

    serie = criador_de_serie(london_df)

    _ = serie.Valor.plot(grid=True)
    plt.show()
