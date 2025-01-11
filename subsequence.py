#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:51:11 2024

@author: meeghageperera
"""

s='abc'
target="deagbnrc"
flag='false'

i=0

char=s[i]

for ele in target:
    

        
    
    
    if ele==char:
        
        if i==len(s)-1:
            flag="True"
            break
        
        
        i+=1
        char=s[i]
        
        
print(flag)
    
    
        