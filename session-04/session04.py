def adding(n1,n2,n3,n4):
    return n1+n2+n3+n4

def Minus(n1,n2):
    return n1-n2

def Dividing (n1,n2):
    if n2==0:
        return "Error:.... "
    else:
        return n1/n2

def Multiplication(n1,n2):
    return n1*n2

#print(n1)
#print(type(n1))
print("Hi, user, this is my calculator\n")
print("You can input 4 numbers then minus the fifth number from the sum of them")
m1=int(input("Please enter the first number:"))
m2=int(input("Please enter the second number:"))
m3=int(input ("Please enter the third number:"))
m4=int(input("Please enter the forth number:"))

m_sum=m1+m2+m3+m4

s=int(input("Please enter the number you want to minus from sum:"))

print("the result of sum of 4 number - fifth number = ",m_sum-s)

























    