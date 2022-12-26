import pandas as pd
import openpyxl
import math
import warnings
import matplotlib.pyplot as plt


file_name = "data.csv"
df = pd.read_csv(file_name, delimiter=";", index_col=["дата"], parse_dates=True)
df.drop(["стоимость", "признак", "НДС", "наличными", "безналичными", "место расчетов", "дата и время", "время"], axis=1, inplace=True)
warnings.simplefilter(action='ignore', category=Warning)

group = df.groupby("товар")
result_df = pd.DataFrame()

print(len(group.groups.keys()))

group_item = group.get_group("святой источник 0,5")
group_item_data = group_item.groupby("дата")
next_column = pd.DataFrame({"святой источник 0,5": []})
for data_key in group_item_data.groups.keys():
    product_count = len(group_item_data.get_group(data_key))
    next_column.loc[data_key] = [product_count]
result_df["святой источник 0,5"] = next_column["святой источник 0,5"]


k = 0
for key in group.groups.keys():
    k += 1
    if k == 327:
        continue
    print(k, key)
    group_item = group.get_group(key)
    group_item_data = group_item.groupby("дата")
    next_column = pd.DataFrame({key: []})

    for data_key in group_item_data.groups.keys():
        product_count = len(group_item_data.get_group(data_key))
        next_column.loc[data_key] = [product_count]

    result_df[key] = next_column[key]
    for i in result_df.index:
        if not i in next_column[key].index:
            result_df[key][i] = 0

    result_df[key] = pd.to_numeric(result_df[key], downcast='integer')


columns_list = list(result_df.columns)
sorted_columns_list = []
result_list = []

for key in columns_list:
    s = result_df[key].sum()
    if s >= 300:
        sorted_columns_list.append((key, s))

sorted_columns_list.sort(key=lambda x: x[1], reverse=True)
# print(sorted_columns_list)

result_list = [item[0] for item in sorted_columns_list]
print(result_list)
print(len(result_list))
print()

result_file_df = pd.DataFrame()

for key in result_list:
    result_file_df[key] = result_df[key]

print(result_file_df)

result_file_df.to_csv("file_test_data3.csv")



