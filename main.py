from get_hyperparameter import get_parameters_and_error
from get_graph_and_forecast import get_forecast, draw_forecast

# вводим название товара
# вводим количество дней для прогноза
# получаем график с прогнозом
# получаем оценку точности

product_name = input()
days_amount = int(input())

output = get_parameters_and_error(product_name, days_amount)
prameters = output[0]
mape_error = output[1]
wape_error = output[2]

predictions = get_forecast(prameters, product_name, days_amount)

print("mape:", mape_error)
print("wape:", wape_error)
draw_forecast(predictions, product_name)





