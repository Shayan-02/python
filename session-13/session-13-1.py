# importing pandas
import pandas as pd
# declare a dictionary
df = pd.read_excel('zara.xlsx')

#---------------
# selecting rows based on condition
#result = df[(df['prices'] <= 10000 ) & ( df['prices'] >=8000 )]
#print('\nResult dataframe :\n', result)
#---------------
df["grade"] = ''
#print(df)


#Assigment
#find grade in this file for next session without loop but you can use "if" if needed
df.loc[df['prices'] < 8000, 'grade'] = 'a'
df.loc[(df['prices'] >= 8000) & (df['prices'] < 10000), 'grade'] = 'b'
df.loc[(df['prices'] >= 10000) & (df['prices'] < 15000), 'grade'] = 'c'
df.loc[(df['prices'] >= 15000) & (df['prices'] < 25000), 'grade'] = 'd'
df.loc[df['prices'] >= 25000, 'grade'] = 'e'

print(df)