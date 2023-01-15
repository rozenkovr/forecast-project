from get_hyperparameter import get_parameters_and_error
from get_graph_and_forecast import get_forecast, draw_forecast


product_name = input("введине наименование товара: ")
days_amount = int(input("введите горизонт прогнозирования в днях: "))
print()

# получаем гипперпараметры для модели и оценку точности
output = get_parameters_and_error(product_name, days_amount)
prameters = output[0]
mape_error = output[1]
wape_error = output[2]

# строим прогноз
predictions = get_forecast(prameters, product_name, days_amount)
rounded_predictions = [round(x) for x in list(predictions)]

# оценка точности по метрикам и значения прогноза
print("прогноз продаж по каждому дню на", days_amount, "дней:")
print("\t", rounded_predictions)
print("суммарный прогноз продаж за", days_amount, "дней:", sum(rounded_predictions))
print("mape:", mape_error * 100, "%")
print("wape:", wape_error * 100, "%")

draw_forecast(predictions, product_name)





