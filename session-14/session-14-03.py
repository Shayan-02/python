# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # making data frame
# data = pd.read_csv("<a href="https://media.geeksforgeeks.org/wp-content/uploads/nba.csv%22,index_col" rel="nofollow"><u>https://media.geeksforgeeks.org/wp-content/uploads/nba.csv",index_col</u></a> ="Name")


# # data.info()
# # data.describe()

# # display
# #print(data.shape )

# # print(data.head())

# # print(data.tail(20))

# data.dropna(inplace=True)

# # percentile list
# # perc = [.20, .40, .60, .80]

# # list of dtypes to include
# # include = ['object', 'float', 'int']

# # calling describe method
# #desc = data.describe(percentiles=perc, include=include)

# # desc = data["Name"].describe()

# # display
# # print(desc)


# #print(data.head())

# print(data.loc[['Avery Bradley', 'R.J. Hunter']])

# print(data.iloc[0:3])

# print(data.loc[["Avery Bradley", "R.J. Hunter"],
#                    ["Team", "Number", "Position"]] )

# all_3_columns = data.loc[:, ["Team", "Number", "Position"]]

# print(data['Number']>80)


# # defining function to check price
# def fun(num):

#     if num<200:
#         return "I love it!"

#     elif num>= 200 and num<400:
#         return "Normal"

#     else:
#         return "High"

# print(data['Number'].apply(fun))

# print(data['Number'].apply(lambda num :"I love it!" if num > 80 else "Normal" ))


def fun(x): return x.upper()


print(fun('ali'))


def fun2(x): return 'Mohammad' if x > 3 else 'Ali'


print(fun2(8))
