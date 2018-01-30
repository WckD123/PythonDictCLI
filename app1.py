import json
import string

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return "\n".join(data[w])
    else:
        return "Word not found. Please recheck!!"

word = input("Please Enter The Word: \n")

print(translate(word))
