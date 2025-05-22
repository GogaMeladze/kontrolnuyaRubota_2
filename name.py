#3 ЗАДАНИЕ!!!

# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# df = pd.read_excel("12.xlsx")  # Укажи свой файл
# X = df["x"]
# Y = df["y"]
# Z = df["z"]
#
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(X, Y, Z, c=Z, cmap='coolwarm')  # Точки окрашены по значению Z
#
# plt.show()


#1 ZADANIYE
# import pandas as pd
#
# # Загрузка Excel файла
# file_path = '12.xlsx'  # Укажите путь к вашему файлу
# data = pd.read_excel(file_path)
#
# # Запрос у пользователя
# query = input("Введите значение для поиска: ")
#
# # Фильтрация данных
# result = data[data.apply(lambda row: row.astype(str).str.contains(query).any(), axis=1)]
#
# # Вывод результата
# if not result.empty:
#     print(result)
# else:
#     print("Данные не найдены.")

# TWO ZADANIYE!!!
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000), index = pd.date_range(
                                '1/1/2000', periods = 1000))
ts = ts.cumsum()
ts.plot()

plt.show()