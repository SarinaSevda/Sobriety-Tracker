# user_model.py - speichert, lädt und verwaltet Nutzerdaten

import sqlite3
import os

class UserData:
    def __init__(self):
        self.name = ""
        self.addictions = []
        self.goal = ""
        self.sobriety_date = None
        self.sobriety_time = "00:00"
        self.note = []

        # Datenbank-Verbindung beim Start
        self.db_path = "userdata.db"
        self._create_table_if_not_exists()

        # Wenn Nutzer schon existiert, lade seine Daten
        if self.name:
            self.load_from_db()

    def get(self, key, default=None):
        return getattr(self, key, default)


    def _create_table_if_not_exists(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''
                      CREATE TABLE IF NOT EXISTS users
                      (
                          name
                          TEXT
                          PRIMARY
                          KEY,
                          addictions
                          TEXT,
                          goal
                          TEXT,
                          sobriety_date
                          TEXT,
                          sobriety_time
                          TEXT
                      )
                      ''')
            conn.commit()

    def save_to_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR REPLACE INTO users (name, addictions, goal, sobriety_date, sobriety_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                self.name,
                ",".join(self.addictions),  # Liste wird zu CSV-String
                self.goal,
                self.sobriety_date,
                self.sobriety_time
            ))
            conn.commit()

    def load_from_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('SELECT addictions, goal, sobriety_date, sobriety_time FROM users WHERE name=?', (self.name,))
            row = c.fetchone()
            if row:
                self.addictions = row[0].split(",") if row[0] else []
                self.goal = row[1]
                self.sobriety_date = row[2]
                self.sobriety_time = row[3]




    def to_dict(self):
        return {
            "name": self.name,
            "addictions": self.addictions,
            "goal": self.goal,
            "sobriety_date": self.sobriety_date,
            "sobriety_time": self.sobriety_time,
            "note": self.note
        }

    def load_from_dict(self, data):
        self.name = data.get ("name", "")
        self.addictions = data.get ("addictions", "[]")
        self.goal = data.get ("goal", "")
        self.sobriety_date = data.get ("sobriety_date", "None")
        self.sobriety_time = data.get ("sobriety_time", "00:00")
        self.note = data.get ("note", "[]")

