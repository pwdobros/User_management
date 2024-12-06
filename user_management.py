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
    list = []
    pesel()
    if not len(pesel) != 11:

    


def validate_regon(regon):

