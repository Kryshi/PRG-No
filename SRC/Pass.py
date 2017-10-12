# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

   

heslo = input("Zadej heslo >")

MALA = "qwertzuiopasdfghjklyxcvbnm"
VELKA = MALA.upper
SPEC = "!@#$%^&*()[]~"
CISLA = "0123456789"

if len(heslo)  < 8:
    print("too short")
    exit(1)
jeMALA = 0
jeVELKA = 0
jeSPEC = 0
jeCISLA = 0
for znak in heslo:
    if znak in MALA:
        jeMALA = 1
        jeVELKA ( znak in VELKA) or jeVELKA


        
    if znak in CISLA:
        jeCISLA = 1
        

print(jeMALA, je VELKA, jeSPEC, jeCISLA)
if jeMALA + jeVELKA + jeSPEC +jeCISLA >=3:
    print("Heslo je v pořádku")
    exit(0)
else:
    print("Too easy")
    exit(3)