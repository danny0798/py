# coding=utf-8

import re
import sys
import os

# 正则匹配电话号码
# phone="13893670000"
phone = input('please give a phone number:')
p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
phonematch = p2.match(phone)

if phonematch:
    print(phonematch.group())
else:
    print("phone number is error!")

