#!/usr/bin/env python
# coding=utf-8

import numpy as np

#读取数据
data = []
with open('Grid, solar, and EV data from three homes.csv', 'r', encoding="utf-8") as file:

    lines = file.readlines()
    for line in lines:

        temp = line.split(',')
        data.append(temp)

#分割表头
header = data[0]
#分割数据
data_np = np.array(data[1:])
#提取日期列
date = data_np[:,0]

#构造纽约市表头
NY_header = header[0:4]
#构造Austin表头
Austin_header = header[0:1] + header[4:7]
#构造Boulder表头
Boulder_header = header[0:1] + header[8:]

#分割纽约市数据
NY_data = data_np[:,0:4]
#写入纽约数据
with open('1-NY.csv', 'w', encoding="utf8") as file:

    file.write(','.join(NY_header) + '\n')
    for line in NY_data:

        file.write(",".join(line) + "\n")


#Austin数据不连续,需要拼接
#data_np[:,0]取的是一位数据;data_np[:,0].reshape(-1,1)
#转化为2维数据,只有一列
#hstack 水平合并
Austin_data = np.hstack((data_np[:,0].reshape(-1,1), data_np[:, 4:7]))
#写入Austin数据
with open('1-Austin.csv', 'w', encoding="utf8") as file:
    file.write(",".join(Austin_header) + "\n")
    for line in Austin_data:
        file.write(",".join(line) + "\n")

#Boulder数据不连续,需要拼接
Boulder_data = np.column_stack((data_np[:,0], data_np[:,7:]))
#写入Boulder数据
with open("1-Boulder.csv", 'w', encoding="utf8") as file:

    file.write(",".join(Boulder_header))
    for line in Boulder_data:

        file.write(",".join(line))



