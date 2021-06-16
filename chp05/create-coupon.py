#!/usr/bin/env python
# coding=utf-8

import string
import random

coupon_dict = {"".join(random.choices(string.printable[:62], k = 7)): 1 for _ in range(500)}

import json
with open("coupon.json", 'w', encoding="utf8") as f:

    json.dump(coupon_dict, f)