import json
import os

account = "userData.json"
user = ""
def newAccount():
    print("NEW ACCOUNT CREATION")
    username = input("Enter in your username: ")
    password = input("Enter in your password: ")

    try:
        with open(account, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    if username in data:
        print("Username already exists.")
        return

    data[username] = password
    makeNewFile(username)

    with open(account, "w") as file:
        json.dump(data, file, indent=4)

    print("Account created successfully.")

def delAccount():
    print("ACCOUNT DELETION")
    username = input("Enter in your username: ")

    try:
        with open(account, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    if username in data:
        delete = input("Are you sure you want to delete this account " + username + " (y/n): ")
        if(delete.lower() == 'y'):
            del data[username]
            filename = username + "_card_collection.json"
            os.remove()
            print(username + " has been deleted")
            
            with open(account, "w") as file:
                json.dump(data, file, indent=4)

        else:
            print(username + " will not be deleted")
    else:
        print(username + " not found")

def login():
    print("Welcome to the card tracker.\n")
    username = input("Enter your username: ")
    with open(account, "r") as file:
        data = json.load(file)
        if username not in data:
            print(username + " is not in our database.")
            return False

        password = input("Please enter your password: ")
        if data[username] == password:
            return True
        else:
            print("Invalid password")
            return False

def addToFile(filename):
    try:
        with open(filename, "r") as file:
            userData = json.load(file)
        if not isinstance(userData, list):
            userData = {}
    except (FileNotFoundError, json.JSONDecodeError):
        userData = {}

    while True:
        card = input("Add card name (or type 'done'): ")
        if card.lower() == "done":
            break
        userData.append(card)

    return userData

def makeNewFile(name):
    filename = name + "_card_collection.json"
    startingData = addToFile(filename)
    try:
        with open(filename, "w") as file:
            json.dump(startingData, file, indent=4)
        print(f"Success! '{filename}' has been created.")
    except IOError as e:
        print(f"An error occurred while creating the file: {e}")

if(login() == False):
    makeAccount = input("Do you want to make a new account?(y/n): ")
    if(makeAccount.lower() == "y"):
        newAccount()
    else:
        print("Bye!")
else:
    print("Welcome")

delAccount()
