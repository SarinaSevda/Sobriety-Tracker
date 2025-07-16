#!/usr/bin/env python3


'''
    wie gehabt: Startpunkt der Anwendung, aber
    nicht mehr das ursprüngliche oldmain.py -- ruft nur das GUI-Setup auf (gui_wizard.py),

    startet tk.Tk(),


'''

import tkinter as tk
from database import user_exists, load_user_data
from gui_wizard import Gui_Wizard
from styles import *
from user_model import UserData
from main_application import MainApplication

gui_wizard_instance = None  # Placeholder für GUI, wenn verwendet


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Willkommen beim Sobriety Tracker!")
    root.geometry("600x600")
    root.resizable(False, False)

    configure_styles()

    if user_exists():  # prüft & lädt eventuell vorhandene Nutzerdaten aus DB -> direkt zur Hauptanwendung
        user_data_dict = load_user_data()
        user_data = UserData()
        user_data.load_from_dict(user_data_dict)
        app = MainApplication(root, user_data)

    else:  # kein Nutzer vorhanden -> startet GUI zur Erfassung
        user_data = UserData()
        app = Gui_Wizard(root, user_data)

    root.mainloop()
