import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX
from metrics import mape, wape, average


def get_forecast(input_parameters, product_name, days_amount):
    test_df = df[product_name]
    all_data_test1 = test_df["2022-02-15":"2022-06-01"]
    train = all_data_test1[:-days_amount]
    test = all_data_test1[-days_amount:]

    parameters = list(input_parameters)
    parameters.append(7)
    order_parametrs = parameters[0:3]
    seasonal_order_parametrs = parameters[3:8]

    model = SARIMAX(train, order=order_parametrs, seasonal_order=seasonal_order_parametrs)
    result = model.fit(disp=False)
    predictions = result.predict(len(train), len(train) + len(test) - 1)

    return predictions


def draw_forecast(predictions, product_name):
    test_df = df[product_name]
    all_data_test1 = test_df["2022-02-15":"2022-06-01"]

    plt.xlabel("дата")
    plt.ylabel("продажи за день")
    plt.title("предсказание продаж на 2 недели")
    plt.plot(all_data_test1)
    plt.plot(predictions)
    plt.grid()
    plt.show()


warnings.simplefilter(action='ignore', category=Warning)
file_name = "data/датасет_для_прогнозирования.csv"
df = pd.read_csv(file_name, index_col=["дата"], parse_dates=True)


