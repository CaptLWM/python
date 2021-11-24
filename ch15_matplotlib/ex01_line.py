import matplotlib.pyplot as plt
import numpy as np

data1 = [10, 14, 19, 20, 25]

#plt.plot(data1)
#plt.show()

x = np.arange(-4.5 , 5, 0.5)
y = 2*x**2 # y = 2x^2

print([x,y])
plt.plot(x,y)
plt.show()