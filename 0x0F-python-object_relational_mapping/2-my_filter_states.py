#!/usr/bin/python3
"""Takes an argument and displays its value"""

import MySQLdb as dbs
from sys import argv


if __name__ == "__main__":
    """Access db and get states"""
    try:
        conn = dbs.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY\
                states.id ASC".format(argv[4]))

        selected = cursor.fetchall()

        for row in selected:
            print(row)

    except dbs.Error as e:
        print("Error:", e)

