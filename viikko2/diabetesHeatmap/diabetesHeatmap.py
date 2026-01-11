import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../diabetes.csv")

correlation = data.corr()
sns.heatmap(correlation, annot=True)
plt.show()