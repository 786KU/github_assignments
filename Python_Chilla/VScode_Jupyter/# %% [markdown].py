# %% [markdown]
# # jupyter notebook in VScode
# 
# This is much better than other jupyter notebook
# You can change the background theme (dark to white) from setting.

# %%
print("python ka chilla with baba ammar")

# %%
awais="my name is awais"
awais

# %%
import numpy as np
x=np.array([1,2,3,3,4,67,3,4])
x

# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# here how to import your dataset to plot and do whatever you like
 
data = pd.read_csv("Iris.csv")
   
print (data.head(10))

# %%
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("Iris.csv")

plt.plot(iris.index, iris["sepal_length"], "r--")
plt.show


# %%
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)


