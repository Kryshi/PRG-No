#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:05:19 2017

@author: ste35218
"""
import random
seznam = [random.randint(0,100) for _ in range(100)]
for i in seznam:
    if i % 7 == 0:
        print(i)
