#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:34:08 2017

@author: ste35218
"""

import random
i = 0

#while i < 10:
    #print(random.randint(0,100))
    #i = i + 1
    
#for i in range (10):
    #print(random.randint(0,100))
    
seznam = []

for i in range (100):
    seznam += [(random.randint(0,100))]

print(seznam)
soucet = 0
for cislo in seznam:
    soucet += cislo
    

print(soucet / len(seznam))

#random number list, write dividable by 7

seznam = []

