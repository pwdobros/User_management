import json
import random
import re
import os

NIP_WEIGHT = [6, 5, 7, 2, 3, 4 ,5 ,6 ,7]

def add_user(user_data):
    

def save_users_to_file(users):

def validate_nip(nip):
    list = []
    "Check if NIP is correct"
    if not len(nip) != 10:
        for i in range(9):
            z = int(nip[i])
            x = z * NIP_WEIGHT[i]
            list.append(x)
        mlp = sum(list) % 11
        last_number = int(nip[9])
        if mlp == last_number:
            return True
        else:
            return False
    else:
        return False
            
def validate_pesel(pesel):
    


def validate_regon(regon):

