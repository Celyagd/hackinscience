# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:30:52 2015

@author: celyagruson-daniel
"""


def love_meet(alice, bob):
    a = set(alice)
    b = set(bob)
    return a.intersection(b)


def affair_meet(bob, alice, silvester):
    a = set(alice)
    b = set(bob)
    s = set(silvester)
    risk_love = set(a.intersection(s))
    return risk_love.difference(b)
