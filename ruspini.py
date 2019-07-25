import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#reading data ruspinpini missing
data_ruspini = np.genfromtxt("ruspini.csv", delimiter=',')
ruspini_missing = np.genfromtxt("data_ruspini_missing.csv", delimiter=',')
missing_df = pd.DataFrame(ruspini_missing)
#imputation
all_df = []
for label, label_missing_df in missing_df.groupby(2):
    all_df.append(label_missing_df.fillna(label_missing_df.mean().round()))
all_df = pd.concat(all_df)
print(all_df)
#visualization
colors = ['red','blue','black','yellow']
df = pd.DataFrame(data_ruspini)
plt.scatter(df[0],df[1],df[2],c=df[2], cmap=matplotlib.colors.ListedColormap(colors))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

plt.scatter(all_df[0],all_df[1],all_df[2],c=all_df[2], cmap=matplotlib.colors.ListedColormap(colors))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()