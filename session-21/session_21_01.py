#Importing required library
# import numpy as np
# import matplotlib.pyplot as plt

# # Creating x axis with range and y axis with Sine
# # Function for Plotting Sine Graph
# x = np.arange(0, 5*np.pi, 0.1)
# y = np.sin(x)

# # Plotting Sine Graph
# plt.plot(x, y, color='green')
# plt.show()

def division(a,b):
    return a/b


while True:
    cmd=input('Do you want to continue? (y/n): ').strip().lower()
    
    if cmd=='n':
        break
    else:
        a=int(input('Please enter a number: '))
        b=int(input('Please enter the second number: '))
        
        try:
            print('a divided by b is = ',division(a,b))
        # except Exception as e :
        #     print (e)
        except ZeroDivisionError :
            print ('The second number must be more than zero')
        
        finally:
            print('This is always executed')