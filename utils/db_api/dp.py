
import sqlite3
from types import NoneType

connect = sqlite3.connect('database.db') 
cursor = connect.cursor()


async def create_db():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INT, nickname TEXT, profits INT NOT NULL DEFAULT 0)")
        connect.commit()
        return True
    except:
        return False

async def check_newbie(user_id):
    cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    rows = cursor.fetchone()
    if  rows == None:
        return False
    else:
        return True



async def newbie_db(user_id, fullname):
    try:
        cursor.execute(f"INSERT INTO users VALUES ({user_id}, '{fullname}', 0)")
        connect.commit()
        return True
    except:
        return False