#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""


if __name__ == "__main__":
    import requests
    f = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(f.text)))
    print("\t- content: {}".format(f.text))
