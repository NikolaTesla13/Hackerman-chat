import sys
import string
import random
import requests
import pretty_errors

args = []
other_token = ""
my_token = ""
status = None

def generate_token():
    token = ""

    for i in range(0, 20):
        token += random.choice(string.ascii_letters + string.digits)
    
    return token

if __name__ == "__main__":

    args = sys.argv
    if len(args) == 2:
        other_token = args[1]

    my_token = generate_token()
    print("Your token is " + my_token)

    if other_token == "":
        print("Enter your friend's token: ", end="")
        other_token = input()

    if other_token != "":
        status = requests.get("http://127.0.0.1:5000/add/"+my_token+"/"+other_token)
        if status.status_code == 200:
            print("Connected sucsessfully!")
    else:
        status = requests.get("http://127.0.0.1:5000/check/"+my_token)
        if status.text != 404:
            other_token = status.text
            print("Connected sucsessfully! Your friend token is " + other_token)
        else:
            print("Error finding friend!")
            sys.exit(-1)
