import matplotlib.pyplot as plt


# initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

y2=[13, 18,39,48]
y3=[13, 19,39,49]
y4=[12, 18,39,48]
y5=[4, 18,24,48]
y6=[13, 18,21,29]

# plotting the data

# fig = plt.figure(figsize =(7, 5), facecolor='g',
#                  edgecolor='b', linewidth=7)

fig, axs=plt.subplots(2,3, figsize =(7, 5))

axs[0,0].plot(x,y, linestyle='--')
axs[0,0].plot(x,y2)
axs[0,0].bar(x,y3, color='black')
axs[0,1].plot(x,y2)
axs[0,2].plot(x,y3)
axs[1,0].bar(x,y4)
explode = [0.1, 0.2, 0, 0]
axs[1,1].pie(y5,labels=x, explode=explode, shadow=True)
axs[1,2].scatter(x,y6)

axs[0,0].set_ylabel('ksdhaskjdhaksdjh')


# plt.plot(x, y, markersize=10, color='black', marker='*', label='Line1')
# plt.plot(x,y2, label='Line2')

# Adding title to the plot
# plt.title("Linear graph", fontsize=25, color="green")


plt.suptitle('sjkdhalkjdhlaskjdhlaksjdhalksj')


# Adding label on the y-axis
plt.ylabel('Y-Axis')

# Adding label on the x-axis
plt.xlabel('X-Axis')

# Setting the limit of y-axis
plt.ylim(0, 60) 

# setting the labels of x-axis
plt.xticks(x, labels=["one", "two", "three", "four"])

# plt.legend(['Line1', 'Line2'])
plt.legend()
# Saving the figure.
plt.savefig("output_for_j.jpg")

plt.show()
