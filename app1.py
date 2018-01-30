import json
from difflib import *

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return "\n".join(data[w])
    elif len(get_close_matches(w,data.keys()))>0:
        return "Did you mean: " + " or ".join(get_close_matches(w,data.keys(),cutoff=0.77))
    else:
        return "Word not found. Please recheck!!"

word = input("Please Enter The Word: \n")

print(translate(word))
