import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


idx = [18, 2, 3, 4]
col = ['skirt', 'hat']

data = {'skirt': [1000, 2000, 3000, 4000], 'hat': [100, 200, 350, 400]}

df = pd.DataFrame(data, index=idx)

df['grade'] = 1

# print(df)

# mean, mode, median, std, var, skew, kurt


# # Create two multidimensional arrays of
# # integer values
# np_arr1 = np.array([[6, 13, 22, 7, 12],
#                     [7, 11, 16, 32, 9]])
# np_arr2 = np.array([[44, 20, 8, 35, 10],
#                     [98, 23, 42, 6, 13]])

# # Print the array values
# print("\nThe values of the first array :\n", np_arr1)
# print("\nThe values of the second array :\n", np_arr2)

# # Create a new array from two arrays based on
# # the conditions
# new_arr = np.where(((np_arr1 % 2 == 0) & (np_arr2 % 2 == 1)),
#                    np_arr1, np_arr2)

# # Print the new array
# print("\nThe filtered values of both arrays :\n", new_arr)

# 0, NaN

# data prepration, data cleaning, data wrangling

# outlier
# ​

file_path = "D:\Projects\computer_science_learning\computer_science\lectures\python\python_for_data_science\class_01\data.csv"

health_data = pd.read_csv(file_path, header=0, sep=",")
print(health_data)

# data_temp=health_data.dropna(axis=0, inplace=True)
# print(data_temp)
# print(health_data)

print(health_data.info())
print(health_data.describe())

health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line'),
# plt.ylim(ymin=0)
# plt.xlim(xmin=0)

# plt.show()

health_data.dropna(axis=0, inplace=True)
print(health_data)
Max_Pulse = pd.to_numeric(health_data["Max_Pulse"])
percentile10 = np.percentile(Max_Pulse, 25)
print(percentile10)
