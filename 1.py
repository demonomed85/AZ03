import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data)
plt.show()