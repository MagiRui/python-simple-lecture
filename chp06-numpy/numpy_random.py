#!/usr/bin/env python
# coding=utf-8

import numpy as np
rdm = np.random.RandomState()
#均匀分布
rand = np.random.rand(2,3)
print(rand)

#标椎状态分布
randn = np.random.randn(2,3)
print(randn)

randint = np.random.randint(1,10, (2,3))
print(randint)

random = np.random.random((2,3))
print(random)

