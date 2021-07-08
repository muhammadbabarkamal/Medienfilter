# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:44:36 2019

@author: muhammad babar kamal
"""

import numpy as np
img=np.array([[15,15,15,40,90,130,130,160,160],
     [15,15,15,40,90,130,130,0,160],
     [15,15,15,40,90,130,130,160,160],
     [15,15,15,40,90,130,130,160,160],
     [15,255,15,40,90,130,130,5,160],
     [15,15,15,40,90,130,130,160,160],
     [15,15,15,40,90,130,130,160,160],
     [15,15,15,40,90,130,130,160,160],
     ])
img1=np.zeros((8,9),int)


    

for i in range(1,len(img)-1):
    for j in range(1,len(img[i])-1):
        temp=np.zeros((9),int)
        index=0
        for r in range(3):
            for c in range(3):
                temp[index]=img[i+r-1][j+c-1]
                index =index+1

        temp.sort()
        med=temp[5]
        img1[i][j]=med
