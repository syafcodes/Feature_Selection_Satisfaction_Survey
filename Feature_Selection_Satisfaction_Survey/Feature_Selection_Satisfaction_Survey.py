import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("train.csv")

corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")

plt.show()

#print(data)
