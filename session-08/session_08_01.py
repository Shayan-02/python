#Session 08, Part 01
import matplotlib.pyplot as plt
import numpy as np


print("Hello, this is a program that shows the article was sold out during 2020.")
print("please write the name of the articles.\n")

# on a daily basis

def show_slaes_per_item_Monthly(n_articles, n_months): 
 
 
    articles=[]
    a=0

    while a<n_articles:
        article=str(input("Please write the name of the article: "))
        articles.append(article)
        a+=1

    print("The name of articles are as follows:\n")
    print(articles)



    months=[]
    sales=[]

    
    i = 0
    while i<n_months:
        month=str(input("Please enter the name of the month: "))
        months.append(month)
        for item in articles:
            message="Please enter the amonunt of ",item,"you sold out in ",month,": "
            sale=float(input(message))
            sales.append(sale)
            print("Month: ", month," Article:", item," Sales: ", sale, "\n")
        
        i+=1


    print("----------------------------------------------------------------------------")
    print ("Articles: ", articles)
    print("Months: ", months)
    print("Sales: ", sales)

    
    
    print("####### Diagram ########## \n")
    x=np.array(articles)
    X_axis = np.arange(len(x))

    
    temp=[]
    
    m=0
    start_idx=0
    end_idx=n_articles
    
    #Please solve the error for next session
    while m<n_months:
                        
        temp=sales[start_idx:end_idx]
                     
        plt.bar(X_axis + ((m-1)* 0.2), temp, 0.4, label = months[m])
        
        m+=1
        
        start_idx=end_idx      
        end_idx=end_idx*m        
        
    
    plt.xticks(X_axis, x)
    plt.xlabel("Articles")
    plt.ylabel("Purchase")
    plt.title("Purchase per Article")
    plt.legend()
    plt.show()
    

        
show_slaes_per_item_Monthly(2,2)