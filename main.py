import json
account = "userData.json"
def newAccount():
    username = input("Enter in your username: ")
    password = input("Enter in your password: ")

def login():
    username = input("Enter your username: ")
    with open(account, "r") as file:
        data = json.load(file)
        for key, value in data.items():
            if(key == username):
                password = input("Please enter your password: ")
                if(value == password):
                    return True
            else:
                print(username + " is not in our database.")
                return False

def addToFile(filename):
    try:
        with open(filename, "r") as file:
            userData = json.load(file)
        if not isinstance(userData, list):
            userData = []
    except (FileNotFoundError, json.JSONDecodeError):
        userData = []

    while True:
        card = input("Add card name (or type 'done'): ")
        if card.lower() == "done":
            break
        userData.append(card)

    return userData

def makeNewFile():
    name = input("Please enter your name: ")
    filename = name + "_card_collection.json"
    startingData = addToFile(filename)
    try:
        with open(filename, "w") as file:
            # indent=4 makes the file human-readable
            json.dump(startingData, file, indent=4)
        print(f"Success! '{name}' has been created.")
    except IOError as e:
        print(f"An error occurred while creating the file: {e}")