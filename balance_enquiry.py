import json
import sqlite3

def get_balance(username, password):
    conn = sqlite3.connect('database.db')   
    data = {"users": []}
    cursor = conn.execute("SELECT * FROM WATSONCREDENTIALS WHERE UNAME = ? LIMIT 1", [username])
    cursor = cursor.fetchone()

    print(cursor)

    if not cursor:
        conn.close()
        return {
            "message": "Your username is wrong!"
        }
    
    if password == cursor[1]:
        conn.close()
        data["users"].append({"username": cursor[0], "password": cursor[1], "balance": cursor[2]})
        return {
            "message": f'Successful login! Your balance is {data["users"][0]["balance"]} VNR (Venusian Rupiah).'
        }
    else:
        conn.close()
        return {
            "message": "Your password is wrong!"
        }
    
    # Will always return this if connection fails.
    return {
        "message": "Wrong username and or password!"
    }
