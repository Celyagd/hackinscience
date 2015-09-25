# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:33:42 2015

@author: celyagruson-daniel
"""
import requests

try:
    r = requests.get('http://mdk.fr/ip')
    text = r.text
    print(text.split('\n')[0])
except:
    print("No internet connectivity.")
