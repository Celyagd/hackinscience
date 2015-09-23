# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import string
r = list(string.ascii_lowercase)
for i, item in enumerate(r):
    for n in r[i + 1:]:
        print(item + n)
