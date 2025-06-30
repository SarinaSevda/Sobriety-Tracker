import sqlite3
import json
import os

# Verbindung zur SQLite-Datenbank herstellen (bzw. erstellen, falls nicht vorhanden)
conn = sqlite3.connect("sobriety.db")
cursor = conn.cursor()

# Tabelle für persönliche Nutzerprofile
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_profile (
    name TEXT,
    addictions TEXT,
    start_time TEXT
)
""")

# Tabelle für tägliche Notizen
cursor.execute("""
CREATE TABLE IF NOT EXISTS daily_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    note TEXT
)
""")

# Tabelle zur Speicherung des zuletzt verwendeten Profils
cursor.execute("""
CREATE TABLE IF NOT EXISTS last_profile (
    name TEXT
)
""")

conn.commit()

def save_profile(name, addictions, start_time):
    """Speichert ein Nutzerprofil in der Datenbank."""
    cursor.execute("DELETE FROM user_profile")
    cursor.execute("INSERT INTO user_profile VALUES (?, ?, ?)",
                   (name, json.dumps(addictions), start_time))
    conn.commit()

def get_profile():
    """Lädt das gespeicherte Nutzerprofil aus der Datenbank."""
    cursor.execute("SELECT * FROM user_profile")
    result = cursor.fetchone()
    if result:
        name, addictions_json, start_time = result
        addictions = json.loads(addictions_json)
        return name, addictions, start_time
    return None

def save_note(date_str, note_text):
    """Speichert eine Notiz für ein bestimmtes Datum."""
    cursor.execute("INSERT INTO daily_notes (date, note) VALUES (?, ?)",
                   (date_str, note_text))
    conn.commit()

def get_note_by_date(date_str):
    """Lädt eine Notiz für ein bestimmtes Datum."""
    cursor.execute("SELECT note FROM daily_notes WHERE date = ?", (date_str,))
    result = cursor.fetchone()
    return result[0] if result else ""

def save_last_profile(name):
    """Speichert den Namen des zuletzt verwendeten Profils."""
    cursor.execute("DELETE FROM last_profile")
    cursor.execute("INSERT INTO last_profile VALUES (?)", (name,))
    conn.commit()

def load_last_profile():
    """Lädt den Namen des zuletzt verwendeten Profils."""
    cursor.execute("SELECT name FROM last_profile")
    result = cursor.fetchone()
    return result[0] if result else None

def close_db():
    """Schließt die Verbindung zur Datenbank."""
    conn.close()
