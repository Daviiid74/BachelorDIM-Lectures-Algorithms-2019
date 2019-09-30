# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:04:32 2019

@author: martidav
"""

"""
Éditeur de Spyder

@author: David.
"""
import numpy as np
import cv2

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

"""
Reverse a table
"""
def reverse_table(table):
    """
    Args: table
    returns: table inverse
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
        
    index = len(table)
    turns = int(index/2)
    for i in range(turns):
        index = index-1
        b = table[i]
        table[i] = table[index]
        table[index] = b
    
    return table


"""
Bounding box
"""

img=cv2.imread('image.png',0)
cv2.imshow('read image', img)
cv2.waitKey()
cv2.destroyAllWindows()


#Création d'une matrice 2D de 10 par 10
matrix=np.zeros((10,10),dtype=np.int32)
matrix[3:6, 4:8] = np.ones((3,4),dtype=np.int32)

for idrow in range(matrix.shape[0]):
    for idcol in range(matrix.shape[1]):
        pixVal=matrix[idrow,idcol]

print(matrix.shape[0])


def roi_bbox(img):
    """
    Args: une image noir avec une tache blanche
    returns: retoune la bbox de la tache blanche
    """
    top = -1
    bottom = -1
    right = -1
    left = -1
    
    table_coordonne = [[1,2],[3,4],[5,6],[7,8]]
    print (table_coordonne)
    for col in range(img.shape[0]):
        for row in range(img.shape[1]):
            if img[row,col]==1:
                if top > row:
                    top = row
                if bottom < row:
                    bottom = row
                if left < col:
                    left = col
                if right > col:
                    right = col
    #chercher le top puis break de meme pour le bottom, left, right
                
                
            
    
    #retourne les coordonnée de chaque angle de ma bbox dans un tableau 4*2
    return table_coordonne

