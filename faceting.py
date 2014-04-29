import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

N = 100
industry = ['a','b','c']
city = ['x','y','z']
ind = np.random.choice(industry, N)
cty = np.random.choice(city, N)
jobs = np.random.randint(low=1,high=250,size=N)
df_city =pd.DataFrame({'industry':ind,'city':cty,'jobs':jobs})

## how many panels do we need?
cols =df_city.city.value_counts().shape[0]
fig, axes = plt.subplots(1, cols, figsize=(8, 8))

for x, city in enumerate(df_city.city.value_counts().index.values):
    data = df_city[(df_city['city'] == city)]
    data = data.groupby(['industry']).jobs.sum()
    print (data)
    print type(data.index)
    left=  [k[0] for k in enumerate(data)]
    right=  [k[1] for k in enumerate(data)]

    axes[x].bar(left,right,label="%s" % (city))
    axes[x].set_xticks(left, minor=False)
    axes[x].set_xticklabels(data.index.values)

    axes[x].legend(loc='best')
    axes[x].grid(True)
    fig.suptitle('Employment By Industry By City', fontsize=20)
plt.show(1)

from ggplot import *

print ggplot(aes(x='city'), data=df_city) + geom_bar() + facet_grid(x=None, y="city", nrow=1)
