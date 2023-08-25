def test():
    print("ayandehbartar")
test()

def test2():
    return "ayandehbartar"

print(test2())

def test3(a, b):
    return a + b
n = test3(4, 5)

def test4(a, b):
    print("result: ", a + b)
test4(4, 5)

# def test5(fname, lname):
#     return fname + lname
# fname = input("enter your first name: ")
# lname = input("enter your last name: ")
# print(f"your fullname is {fname} {lname}")

def test6(a=2,b=4,c=3):
    pass
# test6(c=8)
print(test6())

# docstring
def avg_func(a, b):
    """This function receives two numbers from the user and calculates their average, puts it in avg and prints the avg

    Args:
        a (float): The first number
        b (float): The second number
    """

    return (a + b) / 2

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
print("the average of numbers is " , avg_func(num1, num2))
print(help(avg_func))

def test7(a, b):
    """This function is sum tow number

    Args:
        a (float): _description_
        b (float): _description_
    """

    return a + b

print(test7(5, 6))