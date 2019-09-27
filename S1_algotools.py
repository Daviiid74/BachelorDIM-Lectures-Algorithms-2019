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
def max_value(table):
    """
    Args: liste des valeurs
    returns: la valeur max et sont index dans la table
    Raises ValueError if input param is not a list
    Raises ValueError if Il ne faut pas une liste vide
    Raises ValueError if Il ne faut pas une liste vide
    """
    #test du type de variable
    if not(isinstance(table, list)):
        raise ValueError('max_value, doit etre une list')
    #test si le tableau n'est pas vide
    if len(table)==0:
        raise ValueError("Exception Il ne faut pas une liste vide")
    #test si c'est le bon type de variable dans le tableau
    if not(isinstance(table[0],(int, float))):
        raise ValueError("Exception Il ne faut pas une liste vide")
    
    maxi = 0
    index_maxi = 0
    
    for i in range(len(table)):
        if table[i] > maxi:
            maxi = table[i]
            index_maxi = table.index(maxi)
    
    return maxi, index_maxi

table_test = [1,2,3,4,5,6,7,8,9]

print(max_value(2))

"""
Reverse a table
"""
def reverse_table(table):
    """
    Args:
    returns:
    R
    """



