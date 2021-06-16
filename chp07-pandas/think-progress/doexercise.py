#!/usr/bin/env python
# coding=utf-8

import pandas as pd, numpy as np

df = pd.read_csv('data.csv', parse_dates=True, index_col=[0,1])

print(df.head(10))
print(">>>>>>>>>>.11")
print(df.columns.values)
print(">>>>>>>>>>.22")
#print(df.index.names)
#print(df.T)
df = df.unstack().KWH
print(df.head(10))
df.fillna(np.nan, inplace=True)
print(">>>>>>>>>>.33")
print(df.shape)
#df.to_csv("test_data.csv", encoding="utf8")
for col in range(df.shape[1]):

    df.iloc[:, col][(df.iloc[:, col] - df.mean(axis=1)).abs() > df.std(axis=1) * 3] = np.nan

df_max = df.max(axis = 1)
df_min = df.min(axis = 1)
df_median = df.mean(axis = 1)
df_sum = df.sum(axis = 1)
df_var = df.var(axis = 1)
df_skew = df.skew(axis = 1) #偏度
df_kurt = df.kurt(axis = 1) #峰度

print(df.agg(["max", "min", "mean", "median", "sum", "std", "skew", "kurt"]))

df_diff = df.diff(axis = 1)
df_dff_max = df_diff.max(axis = 1)

print(df.diff(axis=1).agg(["max", "min", "mean", "median", "sum", "std", "skew", "kurt"]))

df_quantile = df.quantile([.05], axis=1)
print(df_quantile)

df_week_diff = df.groupby(df.columns.week, axis = 1).sum().diff(axis = 1)
print(df_week_diff)