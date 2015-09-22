# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import string
r = string.ascii_lowercase
r = "abcde"
for i in r:
    for n in r:
        if (i+n) != (i+n):
            print(i+n)
