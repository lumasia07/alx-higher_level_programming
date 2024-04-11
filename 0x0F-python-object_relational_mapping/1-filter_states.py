#!/usr/bin/python3
"""Filters states with uppercase N"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Filters and displays all states starting with N"""
    try:
        db_connect = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

        cursor = db_connect.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        result = cursor.fetchall()

        for row in result:
            print(row)


        cursor.close()
        db_connect.close()

    except MySQLdb.Error as e:
        print("Error:", e)
