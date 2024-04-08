import matplotlib.pyplot as plt
import numpy as np
x_nums = np.arange(-2,2,0.01)
y_nums = [x*x for x in x_nums]
plt.plot(x_nums, y_nums)
plt.show()
