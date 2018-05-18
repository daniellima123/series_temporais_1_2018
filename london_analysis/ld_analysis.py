import pandas as pd
import matplotlib.pyplot as plt
import os
from statsmodels.graphics.tsaplots import plot_acf
import scipy as sp
import numpy as np

if __name__ == '__main__':


    london_df = pd.read_csv('Matter2013-London.csv', index_col='Date',
                            parse_dates=True).iloc[:,:-1]
    london_df = london_df.applymap(lambda x: None if(x in (-999, 9999)) else x)

    london_df['Maximo'] = london_df.filter(regex="^H").max(axis=1)

    # _ = serie.Valor.plot(grid=True)
    # plt.show()
    autocorrelation = london_df['Maximo'].autocorr()
    vari = 1/len(london_df)
    z = sp.stats.norm.ppf(0.95)
    interval = [-z*np.sqrt(vari), z*np.sqrt(vari)]

    plot_acf(london_df.Maximo, alpha=1, marker='')
    plt.hlines(y = interval, xmin=0, xmax=30)
    plt.show()
    print("A auto correlação dos dados diários é: %4.2f" %(autocorrelation))
