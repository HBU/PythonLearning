import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#https://www.yiibai.com/pandas/python_pandas_visualization.html

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
df.plot.bar(stacked=True)
df.plot.barh(stacked=True)
df.plot.area()
df.plot.scatter(x='a', y='b')
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
plt.show()


