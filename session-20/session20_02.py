import statistics 
import matplotlib.pyplot as plt
# import seaborn as sns


# initializing list 
li = [1, 9, 3, 3, 3,3,3, 2, 5, 2, 1,1,1,4,6,7,9,7,7] 

# 1 1 2 2 3 3 5 9

print ("The average of list values is : ",end="") 
print (statistics.mean(li))

print ('Median of list values is : ', statistics.median(li))

#rememberance of Set data type!!!!!
print('Set of list : ',set(li))

print('Mode of list values is : ',statistics.mode(li))


y=[4,2,5,1,1,1,3,2]
x=list(set(li))

print('x = ',x)
print('y = ',y)

# plt.plot(x,y)


# plt.hist(li, bins=10, color='skyblue', edgecolor='black')
# sns.histplot(li, bins=30, kde=True, color='lightgreen', edgecolor='red')

# plt.show()

print('Varianve: ',statistics.variance(li))
print('Standard Deviation: ',statistics.stdev(li))