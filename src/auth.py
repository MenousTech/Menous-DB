import json
from secrets import token_urlsafe
from pathlib import Path
import os
import getpass
import sys

if sys.platform == "darwin":
    if not os.path.exists("/Library/Caches/.menousdb"):
        os.mkdir("/Library/Caches/.menousdb")
    if not os.path.exists("/Library/Caches/.menousdb/authdata"):
        os.mkdir("/Library/Caches/.menousdb/authdata")
    if not os.path.exists("/Library/Caches/.menousdb/data"):
        os.mkdir("/Library/Caches/.menousdb/data")
    if not os.path.exists("/Library/Caches/.menousdb/authdata/keys.json"):
        with open("/Library/Caches/.menousdb/authdata/keys.json", "w") as file:
            json.dump([], file)
    if not os.path.exists("/Library/Caches/.menousdb/authdata/login.json"):
        with open("/Library/Caches/.menousdb/authdata/login.json", "w") as file:
            json.dump({}, file)
    path = "/Library/Caches/.menousdb/authdata"
    
elif sys.platform == "win32":
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb")
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"+"\\data"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb/data")
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"+"\\authdata"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb\\authdata")
    path = os.getenv("APPDATA")+"\\MenoudDb"+"\\authdata"
    if not os.path.exists(os.path.join(path,"keys.json")):
        with open(os.path.join(path,"keys.json"),"w") as file:
            json.dump([],file)
    if not os.path.exists(os.path.join(path,"login.json")):
        with open(os.path.join(path,"login.json"),"w") as file:
            json.dump({},file)
    path = os.getenv("APPDATA")+"\\MenoudDb"+"\\authdata"
else:
    if not os.path.exists("/usr/local/bin/menousdb"):
        os.mkdir("/usr/local/bin/menousdb")
    if not os.path.exists("/usr/local/bin/menousdb/data"):
        os.mkdir("/usr/local/bin/menousdb/data")
    if not os.path.exists("/usr/local/bin/menousdb/authdata"):
        os.mkdir("/usr/local/bin/menousdb/authdata")
    path="/usr/local/bin/menousdb/authdata"
    if not os.path.exists(os.path.join(path,"keys.json")):
        with open(os.path.join(path,"keys.json"),"w") as file:
            json.dump([],file)
    if not os.path.exists(os.path.join(path,"login.json")):
        with open(os.path.join(path,"login.json"),"w") as file:
            json.dump({},file)


def check_key(key):
    with open(path+'/keys.json') as file:
        data = json.load(file)

    if key in data:
        return True
    else:
        return False

def generate_key():
    with open(path+'/keys.json') as file:
        data = json.load(file)

    key = token_urlsafe(16)

    with open(path+'/keys.json', 'w') as file:
        data.append(key)
        json.dump(data, file, indent=4)

    return key

def signup():
    with open(path + "/login.json", "r") as file:
        data = json.load(file)
    
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~WELCOME TO MENOUSDB~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        uname = input("ENTER A USERNAME: ")
        pw = getpass.getpass("ENTER PASSWORD: ")
        confirm = getpass.getpass("RE-ENTER PASSWORD: ")
        if pw == confirm:
            data[uname] = [pw, generate_key()]
            with open(path + "/login.json", "w") as file:
                json.dump(data, file, indent=4)
            break
        else:
            print("ERROR! PASSWORDS DO NOT MATCH! TRY AGAIN!\n")

def checksignup():
    with open(path + "/login.json", "r") as file:
        data = json.load(file)

    if data == {}:
        print("No users have been created")
        print("Initiating Root User creation")
        signup()

checksignup()

def getuserkey():
    while True:
        uname = input("ENTER YOUR USERNAME: ")
        pw = getpass.getpass("ENTER YOUR PASSWORD: ")
        with open(path + "/login.json", "r") as file:
            data = json.load(file)
        printed=False
        for i in data:
            if i == uname and data[i][0] == pw:
                print("\nYour Key:",data[i][1],"\n")
                printed=True
                break
        if not printed:
            print("Error Credentials do no match\n")
        else:
            break
        
def Login(username, password):
    Path = path
    with open(Path + "/login.json", 'r') as file:
        data = json.load(file)
        for i in data:
            if i == username and data[i][0] == password:
                return data[i][1]
        return False
    
def authenticate():
    print("\nAUTHENTICATING ROOT USER\n")
    while True:
        uname = input("ENTER USRNAME: ").replace(" ", "")
        pw = getpass.getpass("ENTER PASSWORD: ").replace(" ", "")

        if Login(uname, pw) != False:
            print("\nAUTHENTICATION SUCCESSFUL")
            break
        else:
            print("\nAUTHENTICATION FAILURE! TRY AGAIN\n")





