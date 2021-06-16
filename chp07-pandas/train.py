import pandas as pd

train_df = pd.read_csv('train.csv')
print(train_df.head())
print(train_df.info())
print(train_df.describe())
print(train_df.isnull().sum())

test_df = pd.read_csv('test.csv')

full_df = pd.concat([train_df, test_df], ignore_index=True, sort=False)
print(full_df.tail())

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] =['SimHei']
sns.heatmap(full_df.isnull(), cbar=False).set_title(r"缺失值热力图")
plt.show()