#! /usr/bin/env python3
#!/usr/bin/env python
# coding=utf-8

import pandas as pd

df = pd.read_csv("Salaries.csv")
print(df)
print(df.dtypes)
print(df[['salary', 'rank']].dtypes)
print(df.columns)
print(df.axes)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.values)
print(df.head())
print(df.tail())
print(df.describe())
print(df['salary'].mean())
print(df['salary'].median())
print(df.sex.value_counts())
print(df['discipline'].value_counts(ascending=True, normalize=True))
print(df[df.salary >= 130000].count())
print(df[df.salary >= 130000][df.sex == 'Female'].salary.mean())
print(df[5:10])
print(df['salary'])
print(df.loc[5:10, ['rank', 'salary']])
print(">>>>>>>>>>>>.<<<<<<<<<<<<<<<")
print(df.agg({'salary':['max', 'min'], 'service':['mean', 'std']}))
df_rank = df.groupby(['rank'])
print(df_rank)
print(df_rank.mean())
print(df_rank.median())
print(df.groupby('rank')[['salary']].median())
print(df.groupby('rank')[['salary', 'service']].agg(['mean', 'std', 'skew']))
print(">>>>>>>>>>>>>>>.<<<<<<<<<<<<<<")
print(pd.pivot_table(df, index=['rank']))
print(df.pivot_table(index=['rank', 'sex']))
print(df.pivot_table(index=['rank', 'sex']).unstack().stack())
print(df.pivot_table(index=['rank','sex'], values=['salary', 'service']))
import numpy as np
print(df.pivot_table(index=['rank','sex'], values=['salary', 'service'], aggfunc=[np.mean, 'sum']))


