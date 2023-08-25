
import matplotlib.pyplot as plt
import numpy as np


print("Hello dear, this is a program that gets the information of the sales of some articles to show the diagram showing the amount of purchase in 2020\n")
#----------------------------------

print("First please specify your articles \n")
articles=[]



a=1
while a<4 :
    article=str(input("Please write the name of article(item):"))
    articles.append(article)
    a+=1

print(articles)

for article in articles:
    print(article,"\n")

#----------------------------------

#print("Now please input the monthes and their sales. \n")

months=[]
sales=[]


i = 1
while i<3 :
    
    month=str(input("Please enter the month? "))
    months.append(month)
            
    for article in articles:
        
        input_msg="Please input the total sales sold in the store for ", article, " in ", month, ": "
        sale=int(input(input_msg))
        sales.append(sale)
        print("\n")
        print("Month: ",month," - Article: ", article, " - Sale: " ,sale)
    
    i+=1
    
    print("----------------------------------------------------------------------------")

print(months)
print(articles)
print(sales)

sales_of_jan=sales[:3]
sales_of_feb=sales[3:]
    
print(sales_of_jan)
print(sales_of_feb)

print("#######    Diagram ########## \n")
print("Eventually you can see the diagram\n")

   
x=np.array(articles)

y_1=np.array(sales_of_jan)
y_2=np.array(sales_of_feb)


X_axis = np.arange(len(x))

plt.bar(X_axis - 0.2, y_1, 0.4, label = 'January')
plt.bar(X_axis + 0.2, y_2, 0.4, label = 'February')
  
plt.xticks(X_axis, x)
plt.xlabel("Articles")
plt.ylabel("Purchase")
plt.title("Purchase per Article")
plt.legend()
plt.show()



'''
article_len=len(articles)
sales_len=len(sales)

sales_new_diagram=[]

todo
sum_temp=0
for artcle_index in range(0,sales_len,article_len):
        sum_temp+=sales[artcle_index] 
        sales_new_diagram.append(sum_temp)

'''
