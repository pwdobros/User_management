import json
import random
import re
import os

NIP_WEIGHT = [6, 5, 7, 2, 3, 4 ,5 ,6 ,7]
PESEL_WEIGHT = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
REGON_WEIGHT9 = [8, 9, 2, 3, 4, 5, 6, 7]
REGON_WEIGHT14 = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]

def validate_nip(nip): #Input must be a string
    "Check if NIP is correct"
    list = []
    if not len(nip) != 10:
        for i in range(9):
            x = int(nip[i]) * NIP_WEIGHT[i]
            list.append(x)
        if (sum(list) % 11) == int(nip[9]):
            return True
        else:
            return False
    else:
        return False
            






def validate_pesel(pesel): #Input must be a string
    "Checks if pesel is correct"
    list = []
    if len(pesel) != 11:
        return False
    else:
        for i in range(10):
                x = int(pesel[i]) * PESEL_WEIGHT[i]
                list.append(x)
        for i in range (10):
            if len(str(list[i])) > 1:
                list[i] = list[i] % 10
        if len(str(sum(list))) > 1:
            control = 10 - (sum(list) % 10)
        else:
            control = 10 - sum(list)
    if int(control) == int(pesel[10]):
        return True
    else:
        return False
    
def validate_regon(regon): #Input must be a string
    "Checks if regon is correct"
    list = []
    if len(regon) != 9 and len(regon) != 14:
        return False
    else:
        if len(regon) == 9:
            for i in range(len(regon) - 1):
                x = int(regon[i]) * REGON_WEIGHT9[i]
                list.append(x)
            if (sum(list) % 11) == 10:
                control = 0
            else:
                control = sum(list) % 11
            if int(regon[8]) == int(control):
                return True
            else:
                return False
        if len(regon) == 14:
            for i in range(len(regon) - 1):
                x = int(regon[i]) * REGON_WEIGHT14[i]
            control = x % 11
            if int(regon[13]) == int(control):
                return True
            else:
                return False

        
            
        





        
piesel = ("05242008452")
wynik2 = validate_regon(str(input("Coś tamcoś")))
print (wynik2)




            