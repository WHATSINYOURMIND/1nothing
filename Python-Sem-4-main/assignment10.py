import matplotlib.pyplot as plt
import numpy as np

y = np.array([57, 48, 39, 25, 20, 10])
mylabels = ["United states", "China", "Great Britain", "Russia", "Germany", "Japan"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()
