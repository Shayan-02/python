lst=[8,1,2,4,2,5,6,3,5,1,8]

lst_2=["ali", 'mo','me','ali']


# print (set(lst_2))

tp=(1,4,7)

print(type(tp))
print(tp)

del(tp)

print(tp)

x=11

print("this is the id of x: ",id(x), " and x is :", x)

y=x

print("this is the id of y: ",id(y), " and y is :", y)

y=14

print("this is the id of y: ",id(y), " and y is :", y)

print("this is the id of x: ",id(x), " and x is :", x)


x=[1,3,4]

print("this is the id of x: ",id(x), " and x is :", x)

y=x

print("this is the id of y: ",id(y), " and y is :", y)

z=x.copy()

print("this is the id of y: ",id(z), " and y is :", z)