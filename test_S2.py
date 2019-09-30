# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:30:39 2019

@author: martidav
"""

import S1_algotools
import pytest

#test true
def test_max_value_working1():
	tab_list=[1,2,3,4,5,6,7,8,9]
	test, valeur_max=S1_algotools.max_value(tab_list)
	assert test==9

#test true
def test_reverse_table_working1():
	tab_list=[1,2,3,4,5,6,7,8,9]
	test, table_inverse=S1_algotools.reverse_table(tab_list)
	assert test==[9,8,7,6,5,4,3,2,1]