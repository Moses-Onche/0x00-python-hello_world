#!/usr/bin/python3
"""
A script that takes in GitHub credentials
(username and password) calls the API to get
the last 10 commits from most recent to oldest.
"""
from sys import argv
import requests

if __name__ == "__main__":
    URL = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])

    resp = requests.get(URL)
    commit_obj = resp.json()
    try:
        for count in range(10):
            print("{}: {}".format(
                commit_obj[count].get("sha"),
                commit_obj[count].get("commit").get("author").get("name")))
    except IndexError:
        pass
