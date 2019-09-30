# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:30:39 2019

@author: martidav
"""

import S1_algotools
import pytest

def test_max_value_working1():
	tab_list=[1,2,3,4,5,6,7,8,9]
	test, valeur_max=S1_algotools.average_above_zero(tab_list)
	assert test==9