#!/usr/bin/env python
# coding=utf-8

import json
import random

prize = ["一双拖鞋", "一桶花生油", "一瓶水"]

with open('coupon.json', 'r') as file:

    codes = json.load(file, encoding='utf-8')
    key = input("请输入序列号：")
    if key in codes.keys():

        if codes[key] == 1:
            print("此序列号可用\n奖品为".format(random.choice(prize)))
            codes[key] = 0
        else:
            print("抱歉,次序列号不可用!\n奖品已被领取！")
    else:

        print("抱歉,此序列号不可用")
with open('coupon.json', 'w', encoding="utf8") as file:
    json.dump(codes, file)