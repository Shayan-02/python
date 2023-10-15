# importing pandas
import pandas as pd
   
# declare a dictionary
file = { 
 
 'Name' : ['Ankit', 'Swapnil', 'Aishwarya',
          'Priyanka', 'Shivangi', 'Shaurya' ],
   
 'Age' : [22, 20, 21, 19, 18, 22], 
   
 'Stream' : ['Math', 'Commerce', 'Science',
            'Math', 'Math', 'Science'],
   
 'Percentage' : [90, 90, 96, 75, 70, 80] }
   
# create a dataframe
data = pd.DataFrame(file,
                         columns = ['Name', 'Age',
                                    'Stream', 'Percentage'])
# show the Dataframe
#print("Given Dataframe :\n", data)

# selecting rows based on condition
result = data[data['Percentage'] <= 80]

print('\nResult dataframe :\n', result)