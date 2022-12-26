import pandas as pd
import numpy as np
import math
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX


def mape(pred, tst):
    percent_list = []
    for i in range(len(pred)):
        percent_list.append(math.fabs((pred[i] - tst[i]) / tst[i]))

    return sum(percent_list) / len(pred)


def average(ar):
    return sum(ar) / len(ar)


warnings.simplefilter(action='ignore', category=Warning)
file_name = "data/датасет_для_прогнозирования.csv"
df = pd.read_csv(file_name, index_col=["дата"], parse_dates=True)
test_df = df["кофе капучино"]


train_list = [test_df["2022-01-01":"2022-07-01"],
              test_df["2022-01-08":"2022-07-08"],
              test_df["2022-01-15":"2022-07-15"],
              test_df["2022-01-22":"2022-07-22"],

              test_df["2022-02-01":"2022-08-01"],
              test_df["2022-02-08":"2022-08-08"],
              test_df["2022-02-15":"2022-08-15"],
              test_df["2022-02-22":"2022-08-22"],

              test_df["2022-03-01":"2022-09-01"],
              test_df["2022-03-08":"2022-09-08"],
              test_df["2022-03-15":"2022-09-15"],
              test_df["2022-03-22":"2022-09-22"],

              test_df["2022-04-01":"2022-10-01"],
              test_df["2022-04-08":"2022-10-08"],
              test_df["2022-04-15":"2022-10-15"],
              test_df["2022-04-22":"2022-10-22"]
              ]

test_list = [test_df["2022-07-02":"2022-07-08"],
             test_df["2022-07-09":"2022-07-15"],
             test_df["2022-07-16":"2022-07-22"],
             test_df["2022-07-23":"2022-07-29"],

             test_df["2022-08-02":"2022-08-08"],
             test_df["2022-08-09":"2022-08-15"],
             test_df["2022-08-16":"2022-08-22"],
             test_df["2022-08-23":"2022-08-29"],

             test_df["2022-09-02":"2022-09-08"],
             test_df["2022-09-09":"2022-09-15"],
             test_df["2022-09-16":"2022-09-22"],
             test_df["2022-09-23":"2022-09-29"],

             test_df["2022-10-02":"2022-10-08"],
             test_df["2022-10-09":"2022-10-15"],
             test_df["2022-10-16":"2022-10-22"],
             test_df["2022-10-23":"2022-10-29"]
             ]


p_list = [0, 1, 2, 3, 4]
d_list = [2]
q_list = [0, 1, 2, 3, 4]
P_list = [3]
D_list = [0]
Q_list = [1]

mape_list_average = []

for p in p_list:
    for d in d_list:
        for q in q_list:
            for P in P_list:
                for D in D_list:
                    for Q in Q_list:
                        mape_list = []
                        for i in range(15):
                            if (d == 2) and (D == 2):
                                break
                            model = SARIMAX(train_list[i], order=(p, d, q), seasonal_order=(P, D, Q, 7))
                            result = model.fit()

                            predictions = result.predict(len(train_list[i]), len(train_list[i]) + len(test_list[i]) - 1)
                            mape_list.append(mape(predictions, test_list[i]))
                            print("\n", p, d, q, P, D, Q, "\n", "\n")
                        mape_list_average.append(((p, d, q, P, D, Q), average(mape_list)))


for item in mape_list_average:
    print(item)


























