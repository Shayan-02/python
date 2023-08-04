
def check_if_grater_than_Five(n):
    if n>5 :
        print("OK")
    else:
        print("Not OK")
    


def how_are_you(sentence):
    if sentence=="How are you?":
        print ("Fine, thank you! How about you")
    elif sentence=="سلام":
        print("عليک")   
    elif sentence=="Where are you?":
        print("It is my business!") 
    else:
        print("Hey, What have you been up to?")


#check_if_grater_than_Five(3

#how_are_you("Where are you?")



def employment_assessment(age, history, certificate):
    # Note: Certificate means 1:Dimploma, 2 : Bachelor, 3: Master, 4: Doctorate
    
    '''
    history means the years of experience
    certificate means 1:Dimploma, 2 : Bachelor, 3: Master, 4: Doctorate
    '''
    
    if age>=30 and age<=65 and history>=5 and certificate>=2:
        print ("Congratulation!, You are eligible for this job position.")
    else:
        print("The result of assessment is False, Sorry!")


#employment_assessment(29,7,2)




#Variables:
#string
# Number: integer (N, Z ), float(Q ,R)     \
    
n=5
s="Somayeh"
f=51.2
b=True



n1=10
n2=20


#We have 2 types of variables : global, local


n=100

def test(m):
    '''
    the unit of m is meter
    '''
    
    x=15
    
    cm=m*n
    
    
    print(cm)



def test_2():
    print(n+12)


#test_2()


array=[2,4,6,8,10]

print(array)
















