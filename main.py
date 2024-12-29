import tkinter as tk
from tkinter import messagebox


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
        ask_final_welcome()

    else:
        messagebox.showwarning("Warnung"), "Bitte wähle ein Ziel aus."

def ask_goal():
    welcome_label.config(text=f"Willkommen, {user_data['name']}!")
    welcome_label.pack()
    goal_label.pack()
    goal_dropdown.pack()
    goal_button.pack()

def submit_final_welcome():
    messagebox.showinfo("Erfolgreich", f"Sucht: {user_data['addiction']}")
    messagebox.showinfo("Erfolgreich", f"Ziel: {user_data['goal']}")
    root.quit()

def ask_final_welcome():
    final_welcome_label.pack()
    final_welcome_text.pack()
    final_welcome_button.pack()


# Daten speichern
user_data = {}

# Hier die GUI
root = tk.Tk()
root.title('Sobriety Tracker')
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
goal_button = tk.Button(root, text="Abschließen", command=submit_goal)

# Vierte "Abfrage", eher das finale Welcome Window:
final_welcome_label = tk.Label(root, text="Willkommen auf deiner Sobriety-Reise", font=("Helvetica", 12, "bold"))
final_welcome_text = tk.Label(root, text="Im nächsten Schritt zeigen wir dir deinen täglichen Tracker, in dem du deine nüchternen tage verfolgen und dokumentieren kannst und in dem wir dir tägliche Hilfestellungen zur Verfügung stellen.")
final_welcome_button = tk.Button(root, text="Weiter", command=submit_final_welcome)




root.mainloop()

