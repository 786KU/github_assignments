# steps involved in data visualization
# step 1: import libraries

import seaborn as sns
import matplotlib.pyplot as plt

# step 2: set the theme for your graph
sns.set_theme(style="ticks", color_codes=True)

# step 3: import a dataset, you can also import your dataset
kashti = sns.load_dataset("titanic")
# print(kashti) 
# how you can see a summary of your data?

# # # step 4: plot basic graph with 1 variable (countplot)
# p = sns.countplot(x="sex", data=kashti) # countplot mean counting plot, we dont need y axis
# # as it will be count by defaul, we can add other things later, we can specigy other attributes here e.g., hue etc
# plt.show()

# # # step 5: plot basic graph with two variables to show up (countplot), we need to include hue i.e., color
# p = sns.countplot(x="sex", data=kashti, hue="class") # countplot mean counting plot, we dont need y axis
# # as it will be count by defaul, we can add other things later, we can specigy other attributes here e.g., hue etc
# plt.show()

# step 6: plot basic graph with two variables to show up (countplot) with title
p = sns.countplot(x="sex", data=kashti, hue="class") # countplot mean counting plot, we dont need y axis
# as it will be count by defaul, we can add other things later, we can specigy other attributes here e.g., hue etc
p.set_title("Basic plot for kashti")
plt.show()