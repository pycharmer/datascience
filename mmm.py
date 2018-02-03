import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0,20.0, 1000)
print(np.mean(incomes))

plt.hist(incomes, 50)
plt.show()

print(incomes.std())
print(incomes.var())