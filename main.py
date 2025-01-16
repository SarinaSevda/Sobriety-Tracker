import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from mainwindow import *

# Daten speichern
user_data = {}

# Hier kommen die Funktionen hin

def submit_name():
    user_data["name"] = name_entry.get()
    if user_data["name"]:
        # Verstecke Widgets der ersten Abfrage
        name_label.pack_forget()
        name_entry.pack_forget()
        name_button.pack_forget()
        # Zeige Widgets der zweiten Abfrage
        ask_addiction()
    else:
        messagebox.showwarning("Warnung", "Bitte gib deinen Namen ein.")

def submit_addiction():
    user_data["addiction"] = addiction_var.get()
    if user_data["addiction"] != "Bitte auswählen":
        addiction_label.pack_forget()
        addiction_dropdown.pack_forget()
        addiction_button.pack_forget()
        # Zeigt Widgets der nächsten Abfrage
        ask_goal()
    else:
        messagebox.showwarning("Warnung", "Bitte wähle eine Sucht aus.")

def ask_addiction():
    welcome_label.config(text=f"Willkommen, {user_data['name']}!")
    welcome_label.pack()
    addiction_label.pack()
    addiction_dropdown.pack()
    addiction_button.pack()

def submit_goal():
    user_data["goal"] = goal_var.get()
    if user_data["goal"] != "Bitte auswählen":
        goal_label.pack_forget()
        goal_dropdown.pack_forget()
        goal_button.pack_forget()
        # Zeigt Widgets der nächsten Abfrage
        ask_sobriety_duration()

    else:
        messagebox.showwarning("Warnung"), "Bitte wähle ein Ziel aus."

def ask_goal():
    welcome_label.config(text=f"Willkommen, {user_data['name']}!")
    welcome_label.pack()
    goal_label.pack()
    goal_dropdown.pack()
    goal_button.pack()

def submit_sobriety_duration():
    raw_date = sobriety_date.get()
    user_data["sobriety_date"] = raw_date

    user_data["sobriety_time"] = f"{sobriety_hour.get()}:{sobriety_minute.get()}"

    if user_data["sobriety_date"] and user_data["sobriety_time"]:
        sobriety_label.pack_forget()
        sobriety_date.pack_forget()
        sobriety_time_label.pack_forget()
        sobriety_hour_dropdown.pack_forget()
        sobriety_minute_dropdown.pack_forget()
        sobriety_button.pack_forget()

        ask_final_welcome()
    else:
        messagebox.showwarning("Warnung", "Bitte gib ein Datum und eine Zeit an.")

def ask_sobriety_duration():
    sobriety_label.pack()
    sobriety_date.pack()
    sobriety_time_label.pack()
    sobriety_hour_dropdown.pack()
    sobriety_minute_dropdown.pack()
    sobriety_button.pack()

def ask_final_welcome():
    final_welcome_label.pack()
    final_welcome_text.pack()
    final_welcome_button.pack()

# Das fliegt hier wahrscheinlich noch raus
#def submit_final_welcome():
#    messagebox.showinfo("Erfolgreich", f"Sucht: {user_data['addiction']}")
#    messagebox.showinfo("Erfolgreich", f"Ziel: {user_data['goal']}")
#    messagebox.showinfo("Erfolgreich", f"Nüchtern seit: {user_data['sobriety_date']} um {user_data['sobriety_time']}")
#    root.destroy()



def open_main_window():
    """Öffnet das Hauptfenster der Anwendung."""
    main_window(user_data)




# Hier die GUI
root = tk.Tk()
root.title('Sobriety Tracker window 1')
root.geometry('500x500')
root.configure(bg="white")
root.resizable(False, False)

# Erste Abfrage: Wie heißt du?
welcome_label = tk.Label(root, text="Willkommen")
name_label = tk.Label(root, text="Wie heißt du?")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

name_button = tk.Button(root, text="Weiter", command=submit_name)
name_button.pack()

# Zweite Abfrage: Sucht (initial unsichtbar)
welcome_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
addiction_label = tk.Label(root, text="Wähle deine Sucht aus")
addiction_var = tk.StringVar(value="Bitte auswählen")  # Standardwert für das Dropdown
addiction_options = ["Bitte auswählen", "Alkohol", "Zigaretten", "Tierische Produkte", "Drogen", "Kaffee", "Schokolade", "Videospiele"]
addiction_dropdown = tk.OptionMenu(root, addiction_var, *addiction_options)
addiction_button = tk.Button(root, text="Weiter", command=submit_addiction)


#Dritte Abfrage: Ziele
welcome_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
goal_label = tk.Label(root, text="Was möchtest du erreichen?")
goal_var = tk.StringVar(value="Bitte auswählen")
goal_options = ["Weiger Alkohol trinken", "Gesunde Gewohnheiten aufbauen", "Rauchen aufgeben", "Nüchtern bleiben", "Bildschirmzeit reduzieren"]
goal_dropdown = tk.OptionMenu(root, goal_var, *goal_options)
goal_button = tk.Button(root, text="Weiter", command=submit_goal)

#Vierte Abfrage
sobriety_label = tk.Label(root, text="Seit wann bist du nüchtern?")
sobriety_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)

sobriety_time_label = tk.Label(root, text="Um welche Uhrzeit?")
sobriety_hour = tk.StringVar(value="00")
sobriety_hour_dropdown = tk.OptionMenu(root, sobriety_hour, *[f"{i:02}" for i in range(24)])  # Stunden 00-23
sobriety_minute = tk.StringVar(value="00")
sobriety_minute_dropdown = tk.OptionMenu(root, sobriety_minute, *[f"{i:02}" for i in range(60)])  # Minuten 00-59
sobriety_button = tk.Button(root, text="Weiter", command=submit_sobriety_duration)


# Fünfte "Abfrage", eher das finale Welcome Window:
final_welcome_label = tk.Label(root, text="Willkommen auf deiner Sobriety-Reise", font=("Helvetica", 12, "bold"))
final_welcome_text = tk.Label(root, text="Im nächsten Schritt zeigen wir dir deinen täglichen Tracker, in dem du deine nüchternen tage verfolgen und dokumentieren kannst und in dem wir dir tägliche Hilfestellungen zur Verfügung stellen.")
final_welcome_button = tk.Button(root, text="Weiter", command=open_main_window)



root.mainloop()

