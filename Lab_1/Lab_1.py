# -*- coding: cp1251 -*-
import numpy as np

# 1 ������� 
data = np.loadtxt('minutes_n_ingredients.csv', dtype=np.int32, skiprows=1, delimiter=',', )
# ����� ������ 5 ����� �������
print(data[:5])

# 2 �������
#������ ��������
def calculating_min_max_median(data_column):
    minimum = data_column.min()
    maximum = data_column.max()
    median = np.median(data_column)
    mean = np.mean(data_column)

    print("�������: ",minimum)
    print("��������: ", maximum)
    print("�������: ", median)
    print("������� ��������: ", mean)

print("2 �������. \n�������� ��� �����")
calculating_min_max_median(data[:, 1])

print("\n�������� ��� ���������� ������������")
calculating_min_max_median(data[:, 2])


# 3 �������
# ���������� ��������
quantile_75 = np.quantile(data, 0.75)

# ����������� �������� ����������������� ���������� ������� �� �������� q_0.75
data[:, 1] = np.where(data[:, 1] > quantile_75, quantile_75, data[:, 1])


# 4 ������� 
# ������� ���������� �����
count_zero = np.sum(data[:, 1] == 0)
# ������ 0 �� 1 
data[:, 1] = np.where(data[:, 1] == 0, 1, data[:, 1])


# 5 ������� 
# ������� ���������� �������� 
count_uniq_ocbjects = len(np.unique(data[:,0]))

# 6 ������� 
# ������� ��������� �������� ������������
uniq_obj_of_ing = np.unique(data[:,2])

# ���������� ��������� ������������
print("\n6 ������� 6: \n����� ���������� ��������� ������������: ")
print(len(uniq_obj_of_ing)) 
print("\n��������� ����������� \n", uniq_obj_of_ing)


# 7 �������
condition = data[:, 2] <=5 # ������� �������� 
data_limit = data[condition] # �������� ������ �������


# 8 �������
# ���������� �������� ��������
middle_value = data[:, 2] / data[:, 1]

# ������������ ������� ��������
max_value = np.max(middle_value)

print("\n������� 8")
print("������� �������� ��� ������� ������: \n", middle_value)
print("\n������������ ������� ��������: \n", max_value)


# ������� 9
# ���������� �������
sorted_index = np.argsort(data[:, 1]) # ���������� ��������
data = data[sorted_index] # ���������� �������
mid_value_last_100_obj = np.mean(data[-100:, 2])
print("\n������� 8: \n������� ���������� ������������ ��� ���100 ��������: \n", mid_value_last_100_obj)


# ������� 10
# 10 ��������� ������������
random_rows = np.random.randint(0, data.shape[ 0], size=10)
selected_rows = data[random_rows]

print("\n������� 10: \n10 �������� ��������: \n", selected_rows)


# ������� 11
# ������� �������� ������������
average_ingredients = np.mean(data[:, 2])


less_than_average = np.sum(data[:, 2] < average_ingredients)
total_recipes = data.shape[0]

percentage_less_than_average = (less_than_average / total_recipes) * 100

print("������ 11")
print(f"������� �������� � ������������� ����� �������� ������: {percentage_less_than_average:.2f}%")
print() 


#12

# ���������� ������, �����������, ����� ������� "�������"
simple = (data[:, 1] <= 20) & (data[:, 2] <= 5)

# �������������� ����������� ������� � ������������� ������
simple_column = simple.astype(np.int32)

# �������� ������� ������� � ������ ������
data_with_simple = np.column_stack((data, simple_column))

print("������� 12: \n")
print(data_with_simple)
print()



#13


# ������� ������� ��������
percentage_simple = 100 * np.sum(simple) / len(data)

print("13 �������: \n")
print("Percentage of 'simple' recipes: {:.2f}%".format(percentage_simple))
print()



#14

# ���������� �������� � ������ ���������
short = data[data[:, 1] < 10]
standard = data[(data[:, 1] >= 10) & (data[:, 1] < 20)]
long = data[data[:, 1] >= 20]

# ������������ ���������� �������� �� ������ ������
max_short = min(10, len(short))
max_standard = min(10, len(standard))
max_long = min(10, len(long))

# 3d ������
recipes = np.zeros((3, 10, 3), dtype=int)
recipes[0, :max_short, :] = short[:max_short, :]
recipes[1, :max_standard, :] = standard[:max_standard, :]
recipes[2, :max_long, :] = long[:max_long, :]

print("14 �������: \n")
print(recipes.shape)



