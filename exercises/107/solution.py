# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:30:18 2015

@author: celyagruson-daniel
"""


def select_student(my_class, mark_ok):
    from operator import itemgetter
    accepted = []
    refused = []
    my_class_sort = sorted(my_class, key=itemgetter(1))
    for i in my_class_sort:
        if i[1] >= mark_ok:
            accepted.append(i)
        else:
            refused.append(i)
    return {'Accepted': accepted[::-1], 'Refused': refused}
