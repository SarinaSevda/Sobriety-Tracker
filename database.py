import sqlite3
import os
from user_model import UserData

DB_PATH = "userdata.db"

def user_exists(): #prüft, ob Nutzderdaten vorhanden
    if not os.path.exists(DB_PATH):
        return False
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM users")
        result = c.fetchone()
        return result[0] > 0 #mindestens ein Nutzer angelegt

def load_user_data(): #lädt die (ersten) vorhandenen Nutzerdaten rein
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT name, addictions, goal, sobriety_date, sobriety_time FROM users LIMIT 1")
        row = c.fetchone()
        if row:
            return {
                "name": row[0],
                "addictions": row[1].split(",") if row[1] else[],
                "goal": row[2],
                "sobriety_date": row[3],
                "sobriety_time": row[4],
                "note": []
        }
    return None


