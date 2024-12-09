import json
import random
import re
import os

file_path="data/users.json"

NIP_WEIGHT = [6, 5, 7, 2, 3, 4 ,5 ,6 ,7]
PESEL_WEIGHT = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

def load_data():
	if os.path.exists(file_path):
		with open(file_path, "r") as file:
			try:
				data = json.load(file)
				if not isinstance(data, list):
					data = []
			except json.JSONDecodeError:
				data = []
	else:
		data = []
	return data

def add_user(user_data):
	data = load_data()
	if data:
		user_data["id"] = data[-1]["id"] + 1
	else:
		user_data["id"] = 1

	data.append(user_data)
	save_data(data)
     
def check_user():
	username_correct = False
	while username_correct == False:
		user_count = 0
		login_username = input("Podaj imię i nazwisko: ")
		for value in data:
			if value["username"] == login_username:
				username_correct = True
				user_count += 1
				break
		if user_count == 0:
			print("Nazwa użytkownika nieprawidłowa")
	return login_username

def remove_user(user_id):
	"""
	Makes user inactive based on the ID.
	"""
	# Load existing data
	data = load_data()

	for user in data:
		if user["id"] == user_id:
			user.update({"status": "Inactive"})
			break

	save_data(data)
     
def load_user():
	data = load_data()
	for user in data:
		print(f"Id: {user["id"]}\nUsername: {user["username"]}\nNIP: {user["nip"]}\nPESEL: {user["pesel"]}\nREGON: {user["regon"]}\nPassword: {user["password"]}\nStatus: {user["status"]}\n")

def save_data(data):
	"""
	Saves data to .json file.
	"""
	with open(file_path, "w") as file:
		json.dump(data, file, indent=4)

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
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
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

