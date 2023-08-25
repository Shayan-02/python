def condition_2(n1,n2,n3):
    print(n1>n2 or 3==3)

condition_2(10,20,40)



















def condition_inspection(n1,n2,name, food):
    print(n1>n2 and name=="Somayeh", food=="Kebaab Tabe")

#condition_inspection(30,20,"Somayeh","Gheymeh")































def test2(n1, n2):
    
    str1="Muhammad"
    str2="Somayeh"
    
    n=n1+n2 
    
    if n>40:
        result=888
    else:
        result=945
    return result

m=100000+test2(24,568)
#print(m)




def Calculate_sales(year):
    if year <2020:
        result= 40000
    elif year>=2020 and year<2024:
        result=49000
    else: 
        result= 60000
    
    return result
    

def Order(sales_amount):
    if sales_amount>50000:
        result="Ghorneh Sabzi ba Piaz"
    elif sales_amount <50000 and sales_amount>40000:
        result="6leaks"
    else:
        result="KallePaache"
    return result

#mm=Calculate_sales(2018)
#food_for_Muhammad=Order(mm)

food_for_Muhammad=Order(Calculate_sales(2025))

#print(food_for_Muhammad)









'''
def my_add(input1 , input2):
    
    result=input1+input2
    
    return result
print(my_add(10,23))
print("Hi Somayeh")
'''