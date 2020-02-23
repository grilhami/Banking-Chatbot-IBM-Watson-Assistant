#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#

import sys
import json
import sqlite3

"""
    Script to generate table and insert.

    def generate():
        conn.execute('''
                    CREATE TABLE WATSONCREDENTIALS
                    (UNAME VARCHAR(255),
                    PASS VARCHAR(255),
                    BALANCE INT
                    );
                    ''')
        print("Table created successfully!")

        conn.execute("INSERT INTO WATSONCREDENTIALS VALUES ('nicholas', 'nicholas', 10000), ('gilang', 'gilang', 20000);")
        conn.commit()
        print("Records inserted successfully!")

def get_balance(password):
    conn = sqlite3.connect('database.db')   
    data = {"users": []}
    cursor = conn.execute("SELECT BALANCE, PASS FROM WATSONCREDENTIALS WHERE PASS = ? LIMIT 1", [password])

    for row in cursor:
        data["users"].append({"password": password, "balance": row[0]})

    if(data["users"][0]["password"] == password):
        return {
            "balance": data["users"][0]["balance"],
            "message": "It works!"
        }
    else: 
        return {
            "message": "Failed to login!"
        }


    conn.close()
"""

"""
    True function starts here.
"""

def helper(dict):
    conn = sqlite3.connect('database.db')   
    data = {"users": []}
    cursor = conn.execute("SELECT * FROM WATSONCREDENTIALS WHERE UNAME = ? LIMIT 1", [dict['username']])

    # Compare Username and Password
    for row in cursor:
        if dict['username'] == row[0] and dict['password'] == row[1]:
            data["users"].append({"username": dict['username'], "password": dict['password'], "balance": row[2]})

            return {
                "balance": data["users"][0]["balance"],
                "message": "Successful login!"
            }

    return {
        "message": "Wrong username and or password!"
    }

    conn.close()
