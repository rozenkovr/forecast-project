import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX
warnings.simplefilter(action='ignore', category=Warning)


def mape(pred, tst):
    percent_list = []
    for i in range(len(pred)):
        percent_list.append(math.fabs((pred[i] - tst[i]) / tst[i]))
    return sum(percent_list) / len(pred)


def wape(pred, tst):
    test_sum = sum(tst)
    pred_sum = sum(pred)
    return (pred_sum - test_sum) / test_sum


def average(ar):
    return sum(ar) / len(ar)


file_name = "data/датасет_для_прогнозирования.csv"
df = pd.read_csv(file_name, index_col=["дата"], parse_dates=True)
test_df = df["кофе латте"]
train = test_df["2022-02-15":"2022-05-16"]
test = test_df["2022-05-17":"2022-06-01"]


model = SARIMAX(train, order=(2, 2, 4), seasonal_order=(2, 0, 1, 7))
result = model.fit()
predictions = result.predict(len(train), len(train) + len(test) - 1)


print(mape(predictions, test))
print(wape(predictions, test))

mape_graph = []
wape_graph = []

for i in range(len(predictions))[1:]:
    mape_graph.append(mape(predictions[i - 1:i], test[i - 1:i]))
    wape_graph.append(wape(predictions[i - 1:i], test[i - 1:i]))

plt.figure(figsize=(14, 7))
plt.xlabel("дата")
plt.ylabel("ошибка по mape")
plt.title("график ошибки по mape для кофе латте для каждого дня")
plt.plot(mape_graph)
plt.grid()
plt.show()

plt.figure(figsize=(14, 7))
plt.xlabel("дата")
plt.ylabel("ошибка по wape")
plt.title("график ошибки по wape для кофе латте для каждого дня")
plt.plot(wape_graph)
plt.grid()
plt.show()



