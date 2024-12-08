import json
import random
import re
import os

NIP_WEIGHT = [6, 5, 7, 2, 3, 4 ,5 ,6 ,7]
PESEL_WEIGHT = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

def add_user(user_data):
    

def save_users_to_file(users):

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
    
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])


    


def validate_regon(regon):

