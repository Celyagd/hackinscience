# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import sys
if len(sys.argv) > 1:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a-b)
else:
    print("usage: python3 solution.py OP1 OP2")
