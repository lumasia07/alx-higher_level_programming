#!/usr/bin/python3
"""Script that lists all states from a database"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    try:
        """Access and get states from DB"""

        db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

        db_cursor = db_connect.cursor()

        db_cursor.execute("SELECT * FROM states")

        selected = db_cursor.fetchall()

        for row in selected:
            print(row)

        db_cursor.close()
        db_connect.close()

    except MySQLdb.Error as e:
        print("Errot:", e)
