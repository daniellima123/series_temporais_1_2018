import pandas as pd
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':

    files = [x for x in os.listdir(".") if x.endswith(".CSV")]
    print(files)
    df_list = []
    for f in files:

        df = pd.read_csv(f, index_col='Date')
        df_list.append(df)
    df = pd.concat(df_list)
    df.index = pd.to_datetime(df.index, infer_datetime_format=True)
    df.Point.plot()
    plt.show()

