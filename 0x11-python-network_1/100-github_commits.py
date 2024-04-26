#!/usr/bin/python3
"""Lists 10 most recenet commits from a repo"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()

    try:
        for _ in range(10):
            print("{}: {}".format(
                commits[_].get("sha"),
                commits[_].get("commit").get("author").get("name")))
    except IndexError:
        pass
