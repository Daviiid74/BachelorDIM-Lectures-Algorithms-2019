# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

@author: David.
"""
import numpy as np


"""
Test Git gitHub
"""
print('Hello World')

myVariable = 0
print('Myvariable = ', myVariable)


tab_list = [1,2,3,-4,6,-9]
tab_zeros = np.zeros(12, dtype=np.int32)
tab_from_list=np.array(tab_list)

Som = 0
N = 0


for id in range(len(tab_from_list)):
    print('tab['+str(id)+ '=' +str(tab_from_list[id]))
    print('tab[{index}]={val}'.format(index=id, val=tab_from_list[id]))
    
    if tab_from_list[id] >0:
        print('Youpi')

print('Finished')

"""
Exercice 1
"""

som = 0
n = 0
moy = 0
nmax = [1,2,3,-4,6,-9]

for i in range(len(nmax)):
    if nmax[i] > 0:
        som = som + nmax[i]
        n = n + 1

moy = som/n
print(moy)
print('fini')

