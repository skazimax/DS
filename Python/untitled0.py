# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:55:30 2017

@author: mrasskazov
"""
import numpy as np
def m_det(x):
    if x.shape==(2,2):
        m=x[0,0]*x[1,1]-x[0,1]*x[1,0]
        return m
    
    else:
        m=0
        for i in range(len(x)):
            m+=x[0,i]*(-1)**(2+i)*m_det(np.delete(np.delete(x,0,0),i,1))
        return m
    
    
        
        
