import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

midwest = pd.read_csv(r'midwest_filter.csv')

categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i / float(len(categories) - 1)) for i in range(len(categories))]

plt.figure(figsize=(16, 10))

for i, category in enumerate(categories):
    plt.scatter('percbelowpoverty','perchsd', data=midwest.loc[midwest.category == category, :]
                , s=20
                , c=np.array(colors[i]).reshape(1, -1)
                , label=str(category))
plt.title("Relationship between the proportion of high school diplomas and the proportion of poor people",fontsize = 18)
plt.xlabel('Poverty population proportion',fontsize = 15)
plt.ylabel('Percentage with a high school diploma',fontsize = 15)
plt.legend(loc='upper right')

plt.show()
