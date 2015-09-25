# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:47:53 2015

@author: celyagruson-daniel
"""

with open('words') as f:
    read_f = f.read()
    print(len(read_f))
    count = 0
    for i in read_f:
        if 'e' in i:
            count = count + 1
    print(count)
