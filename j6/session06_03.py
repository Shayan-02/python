import matplotlib.pyplot as plt
import numpy as np


items=["Shirt","Perfume","Shoes"]
sales=[20000, 70000, 120000]


x=np.array(items)
y=np.array(sales)

plt.bar(x,y,color="yellow")
plt.show()

