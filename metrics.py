import math


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
