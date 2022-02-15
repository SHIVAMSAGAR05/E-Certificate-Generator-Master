# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:51:38 2020

@author: SHIVAM
"""


import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        yn =  input("Did you mean %s instead ? Enter Y if yes , or N if no:" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist, Please check the word"
        else:
            return "We don't understand your word please check it out"
    else:
        return "The word doesn't exist, please check the spelling"
word = input("Enter The word to define : ")

output = (translate(word))

if type(output) == list:
    for items in output:
        print(output)

else:
    print(output)
        