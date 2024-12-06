import json
import random
import re
import os

NIP_WEIGHT = [6, 5, 7, 2, 3, 4 ,5 ,6 ,7]

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
            
def validate_pesel(pesel):
    "Checks if pesel is correct"
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    


def validate_regon(regon):

