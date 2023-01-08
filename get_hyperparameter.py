import pandas as pd
import numpy as np
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX
from metrics import mape, wape, average
from get_graph_and_forecast import get_forecast


def get_parameters_and_error(product_name, days_amount):
    test_df = df[product_name]
    all_data_test1 = test_df["2022-02-15":"2022-06-01"]
    train1 = all_data_test1[:- days_amount]
    test1 = all_data_test1[- days_amount:]

    all_data_test2 = test_df["2022-07-10":"2022-10-24"]
    train2 = all_data_test2[:- days_amount]
    test2 = all_data_test2[- days_amount:]

    all_data_test = all_data_test1
    train = train1
    test = test1

    p_list = [0, 1, 2, 3, 4]
    d_list = [2]
    q_list = [0, 1, 2, 3, 4]
    P_list = [3]
    D_list = [0]
    Q_list = [1]

    mape_list = []

    for p in p_list:
        for d in d_list:
            for q in q_list:
                for P in P_list:
                    for D in D_list:
                        for Q in Q_list:
                            model = SARIMAX(train, order=(p, d, q), seasonal_order=(P, D, Q, 7))
                            result = model.fit(disp=False)

                            predictions = result.predict(len(train), len(train) + len(test) - 1)
                            mape_list.append(((p, d, q, P, D, Q), round(mape(predictions, test), 4),
                                              round(wape(predictions, test), 4)))
                            print(p, d, q, P, D, Q)

    sorted_list = sorted(mape_list, key=lambda tup: tup[1] + tup[2] * 0.3)
    return sorted_list[0]


warnings.simplefilter(action='ignore', category=Warning)
file_name = "data/датасет_для_прогнозирования.csv"
df = pd.read_csv(file_name, index_col=["дата"], parse_dates=True)

