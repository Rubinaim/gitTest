import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
exp = lambda x: np.exp(x) 
sin = lambda x: np.sin(x)
cos = lambda x: np.cos(x)

plt.plot(x, cos(x))
plt.plot(x, sin(x))
plt.show()
