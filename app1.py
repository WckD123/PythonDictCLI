import json
from difflib import *

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        print("\n".join(data[w]))
    elif len(get_close_matches(w,data.keys()))>0:
        new_word = get_close_matches(w,data.keys())[0]
        print("Did you mean: " + new_word)
        check = input("Enter y or n: ")
        check = check.lower()
        if check == "yes" or check == "y":
            print("\n".join(data[new_word]))
        else:
            meaning()
    else:
        print("Word not found. Please recheck!!")

def meaning():
    word = input("Please Enter The Word: \n")
    translate(word)

meaning()
