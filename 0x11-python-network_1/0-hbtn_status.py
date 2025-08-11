#!/usr/bin/python3
"""
This module fetches the page at https://alx-intranet.hbtn.io/status using urllib,
reads the response body, and prints it with each line preceded by a tab.
"""

from urllib import request


def fetch_status():
    """
    Fetches the content from https://alx-intranet.hbtn.io/status using urllib
    and prints the body with a tab before each line.
    """
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read().decode("utf-8")
        print("Body response:")
        for line in body.splitlines():
            print(f"\t- {line}")


if __name__ == "__main__":
    fetch_status()

