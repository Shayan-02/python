import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def my_function(x):
    return 2*x + 80


print(my_function(10))


file_path = "D:\Projects\computer_science_learning\computer_science\lectures\python\python_for_data_science\class_01\data.csv"

health_data = pd.read_csv(file_path, header=0, sep=",")

print(health_data['Duration'].std())
