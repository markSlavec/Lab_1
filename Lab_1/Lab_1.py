# -*- coding: cp1251 -*-
import numpy as np

# 1 Задание 
data = np.loadtxt('minutes_n_ingredients.csv', dtype=np.int32, skiprows=1, delimiter=',', )
# Вывод первых 5 строк массива
print(data[:5])

# 2 Задание
#Расчет значений
def calculating_min_max_median(data_column):
    minimum = data_column.min()
    maximum = data_column.max()
    median = np.median(data_column)
    mean = np.mean(data_column)

    print("Минимум: ",minimum)
    print("Максимум: ", maximum)
    print("Медиана: ", median)
    print("Среднее значение: ", mean)

print("2 задание. \nЗначения для минут")
calculating_min_max_median(data[:, 1])

print("\nЗначения для количества ингредиентов")
calculating_min_max_median(data[:, 2])


# 3 Задание
# Вычисления квантиля
quantile_75 = np.quantile(data, 0.75)

# Ограничение значений продолжительности выполнения рецепта по квантилю q_0.75
data[:, 1] = np.where(data[:, 1] > quantile_75, quantile_75, data[:, 1])


# 4 Задание 
# Подсчет количества нулей
count_zero = np.sum(data[:, 1] == 0)
# Замена 0 на 1 
data[:, 1] = np.where(data[:, 1] == 0, 1, data[:, 1])


# 5 Задание 
# Подсчет уникальных рецептов 
count_uniq_ocbjects = len(np.unique(data[:,0]))

# 6 Задание 
# Подсчет различных значений ингредиентов
uniq_obj_of_ing = np.unique(data[:,2])

# Количество различных ингредиентов
print("\n6 Задание 6: \nОбщее количество различных ингредиентов: ")
print(len(uniq_obj_of_ing)) 
print("\nРазличные ингредиенты \n", uniq_obj_of_ing)


# 7 Задание
condition = data[:, 2] <=5 # Условие проверки 
data_limit = data[condition] # Создание нового массива


# 8 Задание
# Вычисление среднего значения
middle_value = data[:, 2] / data[:, 1]

# Максимальное среднее значение
max_value = np.max(middle_value)

print("\nЗадание 8")
print("Среднее значение для каждого рецепт: \n", middle_value)
print("\nМаксимальное среднее значение: \n", max_value)


# Задание 9
# Сортировка массива
sorted_index = np.argsort(data[:, 1]) # Сортировка индексов
data = data[sorted_index] # Сортировка массива
mid_value_last_100_obj = np.mean(data[-100:, 2])
print("\nЗадание 8: \nСреднее количество ингредиентов для топ100 рецептов: \n", mid_value_last_100_obj)


# Задание 10
# 10 случайных ингредиентов
random_rows = np.random.randint(0, data.shape[ 0], size=10)
selected_rows = data[random_rows]

print("\nЗадание 10: \n10 случаных рецептов: \n", selected_rows)


# Задание 11
# Среднее значение ингредиентов
average_ingredients = np.mean(data[:, 2])


less_than_average = np.sum(data[:, 2] < average_ingredients)
total_recipes = data.shape[0]

percentage_less_than_average = (less_than_average / total_recipes) * 100

print("Задние 11")
print(f"Процент рецептов с ингредиентами менее среднего уровня: {percentage_less_than_average:.2f}%")
print() 


#12

# логический массив, указывающий, какие рецепты "простые"
simple = (data[:, 1] <= 20) & (data[:, 2] <= 5)

# Преобразование логического массива в целочисленный массив
simple_column = simple.astype(np.int32)

# Добавить простой столбец в массив данных
data_with_simple = np.column_stack((data, simple_column))

print("Задание 12: \n")
print(data_with_simple)
print()



#13


# процент простых рецептов
percentage_simple = 100 * np.sum(simple) / len(data)

print("13 Задание: \n")
print("Percentage of 'simple' recipes: {:.2f}%".format(percentage_simple))
print()



#14

# количество рецептов в каждой категории
short = data[data[:, 1] < 10]
standard = data[(data[:, 1] >= 10) & (data[:, 1] < 20)]
long = data[data[:, 1] >= 20]

# максимальное количество рецептов из каждой группы
max_short = min(10, len(short))
max_standard = min(10, len(standard))
max_long = min(10, len(long))

# 3d массив
recipes = np.zeros((3, 10, 3), dtype=int)
recipes[0, :max_short, :] = short[:max_short, :]
recipes[1, :max_standard, :] = standard[:max_standard, :]
recipes[2, :max_long, :] = long[:max_long, :]

print("14 Задание: \n")
print(recipes.shape)



