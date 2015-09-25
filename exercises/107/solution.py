# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:02:45 2015

@author: celyagruson-daniel
"""

from operator import itemgetter

my_class = [['Kermit Wade', 27],
            ['Hattie Schleusner', 67],
            ['Ben Ball', 5],
            ['Cen Ball', 5],
            ['William Lee', 2]]

            
def select_student(my_class, mark_ok):
    accepted = []
    refused = []
    my_class_sort = sorted(my_class, key=itemgetter(1))
    for i in my_class_sort:
        if i[1] >= mark_ok:
            accepted.append(i)
        else:
            refused.append(i)
    return {'Accepted': accepted[::-1], 'Refused': refused}
