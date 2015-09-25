# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:03:11 2015

@author: celyagruson-daniel
"""
import string
import re

s = ""
with open('words') as f:
    s += f.read()

s = s.replace("\n", "").replace("\'", "")

for l in string.ascii_lowercase:
    a = re.findall(l, s)
    print("{}: {:.2f}".format(l, float(len(a)) / len(s)))
