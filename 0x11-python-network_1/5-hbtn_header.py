#!/usr/bin/python3
"""
A Script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]
    req = requests.get(URL)
    print(req.headers.get("X-Request-Id"))
