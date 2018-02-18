import numpy as np
import matplotlib.pyplot as plt

success = []

for i in range(100000):
    experiment = (np.random.random(size=10))
    success.append(sum(experiment > 0.5))

plt.hist(success)
plt.show()