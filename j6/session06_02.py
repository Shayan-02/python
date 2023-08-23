

'''
This project woks as follows:
    It gets your information and return you the result of assessment in order to hire in our company.
'''
def assessment(name, experience, gpa):
    print ("\n",name," thank you for your application,\n")
    if experience<1 :
        print ("You have ", experience ," year(s) of experience, and GPA: ",gpa, " ,so you can join us as an internship!")
    elif  experience<=3 and gpa<=15 :
        print ("You have ", experience ," year(s) of experience, and GPA: ",gpa, " ,so you can join us as a junior!")
    elif experience <=3 and gpa>15:
        print("You have ", experience ," year(s) of experience, and GPA: ",gpa, " ,so you can join us as a pre-senior!")
    elif experience >3 and  experience <10 and gpa>13:
        print("You have ", experience ," year(s) of experience, and GPA: ",gpa, " ,so you can join us as a pre-senior!")
    else:
        print ("You have ", experience ," year(s) of experience, and GPA: ",gpa, " ,so you can join us as a manager!")

i=True
while i:
    print ("Welcome!", " Please insert your information:\n")
    name= input("Please insert your name: ")
    #degree=int(input("Please insert your degree (1=Diploma, 2=Bachelor, 3=Master, 4= Doctorate ): "))
    gpa=float(input("Please insert your GPA : "))
    experience=int(input ("Please insert your years of experience: "))
    
    assessment(name,experience,gpa)
      
    
    x=str(input("\n Do you want to exit the program? (Y?N) "))
    print("-----------------------------------------")
    
    if x=="Y":
        i=False
    
    

    