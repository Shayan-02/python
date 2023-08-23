
#This is Mohammad's program

print("Please answer following questions for hiring in this company.\n")

"""

print("Please insert 5 Degree.\n")
print(" Degree means 1:Dimploma, 2 : Bachelor, 3: Master, 4: Doctorate.\n")
Degree1=float(input("Please insert the number that related your DEGREE: "))
Degree2=float(input("Please insert the number that related your DEGREE: "))
Degree3=float(input("Please insert the number that related your DEGREE: "))
Degree4=float(input("Please insert the number that related your DEGREE: "))
Degree5=float(input("Please insert the number that related your DEGREE: "))

list_Degree = [Degree1,Degree2,Degree3,Degree4,Degree5]

"""
print("Please insert 5 Names.\n")
NAME1=str(input("please insert the first Name: "))
NAME2=str(input("please insert the second Name: "))
NAME3=str(input("please insert the third Name: "))
NAME4=str(input("please insert the forth Name: "))
NAME5=str(input("please insert the fifth Name: "))
list_Name = [NAME1,NAME2,NAME3,NAME4,NAME5]
##

print("\n Please insert 5 GPA.\n")
Avarage1=float(input("PLease insert your Aoademic GPA: "))
Avarage2=float(input("PLease insert your Aoademic GPA: "))
Avarage3=float(input("PLease insert your Aoademic GPA: "))
Avarage4=float(input("PLease insert your Aoademic GPA: "))
Avarage5=float(input("PLease insert your Aoademic GPA: "))
list_Avarage = [Avarage1,Avarage2,Avarage3,Avarage4,Avarage5]

##
print("\n Please insert 10 Experiences.\n")
Experiance1=int(input("How many years do you have experiance: "))
Experiance2=int(input("How many years do you have experiance: "))
Experiance3=int(input("How many years do you have experiance: "))
Experiance4=int(input("How many years do you have experiance: "))
Experiance5=int(input("How many years do you have experiance: "))
list_Experiance = [Experiance1,Experiance2,Experiance3,Experiance4,Experiance5]

i=0
while i<5:
    print ("\n",list_Name[i]," thank you for your application,\n")
    if list_Experiance[i]<1 :
        print ("You have ", list_Experiance[i] ," year(s) of experience, so you can join us as an internship!")
    elif  list_Experiance[i]<=3 and list_Avarage[i]<=15 :
        print ("You have ", list_Experiance[i] ," year(s) of experience, so you can join us as a junior!")
    elif list_Experiance[i] <=3 and list_Avarage[i]>15:
        print("You have ", list_Experiance[i] ," year(s) of experience, so you can join us as a pre-senior!")
    elif list_Experiance[i] >3 and  list_Experiance[i] <10 and list_Avarage[i]>13:
        print("You have ", list_Experiance[i] ," year(s) of experience, so you can join us as a pre-senior!")
    else:
        print ("You have ", list_Experiance[i] ," year(s) of experience, so you can join us as a manager!")

    i+=1
    


















'''
for experience in list_Experiance:
    if experience<1 :
        print ("You have ", experience ," year(s) of experience, so you can join us as an internship!")
    elif  experience <=3 :
        print ("You have ", experience ," year(s) of experience, so you can join us as a junior!")
    elif experience <=10:
        print("You have ", experience ," year(s) of experience, so you can join us as a senior!")
    else:
        print ("You have ", experience ," year(s) of experience, so you can join us as a manager!")

'''

# Thank you Mohammad, due to your experience that is 1 and your GPA that is 15 you can join us  as a internship