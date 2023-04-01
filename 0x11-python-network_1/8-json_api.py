#!/usr/bin/python3
"""
A script that takes in a letter sends POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) == 1:
        entry = ""
    else:
        entry = argv[1]
    letter = {"q": entry}

    resp = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        response = resp.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
