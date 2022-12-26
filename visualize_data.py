import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX


def mape(pred, tst):
    percent_list = []
    for i in range(len(pred)):
        percent_list.append(math.fabs((pred[i] - tst[i]) / tst[i]))

    return sum(percent_list) / len(pred)


def wape(pred, tst):
    test_sum = sum(tst)
    pred_sum = sum(pred)
    return math.fabs((pred_sum - test_sum) / test_sum)


def average(ar):
    return sum(ar) / len(ar)


warnings.simplefilter(action='ignore', category=Warning)
file_name = "data/датасет_для_прогнозирования.csv"
df = pd.read_csv(file_name, index_col=["дата"], parse_dates=True)
test_df = df["кофе капучино"]


all_data_test1 = test_df["2022-02-15":"2022-06-01"]
train1 = test_df["2022-02-15":"2022-05-16"]
test1 = test_df["2022-05-17":"2022-06-01"]

all_data_test2 = test_df["2022-07-10":"2022-10-24"]
train2 = test_df["2022-07-10":"2022-10-08"]
test2 = test_df["2022-10-09":"2022-10-24"]

all_data_test = all_data_test1
train = train1
test = test1


model = SARIMAX(train, order=(3, 2, 1), seasonal_order=(2, 0, 1, 7))
result = model.fit()
predictions1 = result.predict(len(train), len(train) + len(test) - 1)

model2 = SARIMAX(train2, order=(3, 2, 1), seasonal_order=(2, 0, 1, 7))
result2 = model2.fit()
predictions2 = result2.predict(len(train2), len(train2) + len(test2) - 1)

print(mape(test, predictions1))
print(wape(test, predictions1))

plt.xlabel("дата")
plt.ylabel("продажи за день")
plt.title("предсказание продаж на 2 недели")
plt.plot(all_data_test1)
plt.plot(predictions1)
plt.grid()
plt.show()
