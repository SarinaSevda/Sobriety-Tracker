from tkinter import messagebox
from tkcalendar import DateEntry
from mainwindow import *
from tkinter import ttk


# Daten speichern
user_data = {}
# Liste für zusätzliche Süchte
additional_addictions = []

# Globale Platzhalter-Initialisierungen für dynamisch erzeugte GUI-Elemente
addiction_frame = None
addiction_dropdown = None
add_addiction_button = None
pack_forget = None
current_step = 1 #trackt, welcher Schritt in der Abfrage gerade aktiv ist

# Style
style = ttk.Style()
style.theme_use('alt')


# Enter-Taste Handler
def on_enter_press(event):
    if current_step == 1:
        submit_name()
    elif current_step == 2:
        submit_addiction()
    elif current_step == 3:
        submit_goal()
    elif current_step == 4:
        submit_sobriety_duration()
    elif current_step == 5:
        open_main_window()


# Zurück-Funktionen
def go_back_to_name():
    global current_step, additional_addictions
    current_step = 1

# Versteckt aktuelle Widgets
    welcome_label.pack_forget()
    addiction_label.pack_forget()
    if addiction_frame:
        addiction_frame.pack_forget()
    addiction_button.pack_forget()
    back_button_2.pack_forget()

# Löscht zusätzliche Süchte und setzt Hauptsucht zurück
    additional_addictions.clear()
    addiction_var.set("Bitte auswählen")

# Zeigt Name-Widgets
    name_label.pack(pady=50)
    name_entry.pack(pady=10)
    name_entry.delete(0, tk.END)  #Löscht vorherigen Namen
    name_entry.insert(0, user_data.get("name", ""))  #Lädt gespeicherten Namen
    name_entry.focus()  #Setzt Fokus auf Eingabefeld
    name_button.pack()


def go_back_to_addiction(): #zurück-Button 1
    global current_step, additional_addictions, addiction_frame, addiction_dropdown, add_addiction_button
    current_step = 2

# Versteckt aktuelle Widgets
    goal_label.pack_forget()
    goal_dropdown.pack_forget()
    goal_button.pack_forget()
    back_button_3.pack_forget()

# Entfernt alle alten zusätzlichen Dropdowns
    for _, dropdown in additional_addictions:
        dropdown.destroy()
    additional_addictions.clear()

# Zerstört veraltetes addiction_frame komplett
    if addiction_frame:
        addiction_frame.destroy()

# Zeigt Sucht-Widgets (Auswahl)
    welcome_label.config(text=f"Willkommen, {user_data['name']}! Bitte wähle deine Süchte aus.")
    welcome_label.pack(pady=50)
    addiction_label.pack()

# Erstellt das addiction_frame neu
    addiction_frame = ttk.Frame(root)
    addiction_frame.pack(pady=10)

    first_row = ttk.Frame(addiction_frame)
    first_row.pack(pady=5)

# Lädt gespeicherte Süchte zurück
    if "addictions" in user_data and user_data["addictions"]:
        saved_addictions = user_data["addictions"]

# Suchtauswahl1 im Dropdownmenü
        if len(saved_addictions) > 0:
            addiction_var.set(saved_addictions[0])
        else:
            addiction_var.set("Bitte auswählen")
    else:
        addiction_var.set("Bitte auswählen")

# Erstellt Hauptdropdown mit Suchtoptionen
    addiction_dropdown = ttk.OptionMenu(first_row, addiction_var, addiction_var.get(), *addiction_options)
    addiction_dropdown.pack(side="left", padx=5)

# Und '+'-Button
    add_addiction_button = ttk.Button(first_row, text="+", command=open_new_addiction_choice)
    add_addiction_button.pack(side="left", padx=5)

# Extra Dropdown(s) für mehr Süchte
    if "addictions" in user_data and len(user_data["addictions"]) > 1:
        for i in range(1, len(user_data["addictions"])):
            new_var = tk.StringVar(root, value=user_data["addictions"][i])
            new_dropdown = ttk.OptionMenu(addiction_frame, new_var, new_var.get(), *addiction_options)
            new_dropdown.pack(pady=5)
            additional_addictions.append((new_var, new_dropdown))

    addiction_button.pack()
    back_button_2.pack()


def go_back_to_goal():
    global current_step
    current_step = 3

    # Versteckt aktuelle Widgets
    sobriety_label.pack_forget()
    sobriety_date.pack_forget()
    sobriety_time_label.pack_forget()
    sobriety_hour_dropdown.pack_forget()
    sobriety_minute_dropdown.pack_forget()
    sobriety_button.pack_forget()
    back_button_4.pack_forget()

    # Zeigt Ziel-Widgets
    welcome_label.config(text="Super! Was möchtest du erreichen?")
    welcome_label.pack(pady=50)
    goal_label.pack()
    goal_dropdown.pack(pady=10)

    # Lädt gespeicherte Zielauswahl zurück
    if "goal" in user_data:
        goal_var.set(user_data["goal"])

    goal_button.pack()
    back_button_3.pack()


# Hauptfunktionen
def submit_name():
    """Abfrage und Einreichen des Namen"""
    global current_step
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

def ask_addiction():
    """Abfrage der Sucht"""
    welcome_label.config(text=f"Willkommen, {user_data['name']}! \nBitte wähle deine Süchte aus.", wraplength=500, justify="center")
    welcome_label.pack(pady=50)

    addiction_label.pack()

    global addiction_frame
    addiction_frame = ttk.Frame(root)
    addiction_frame.pack(pady=10)

    first_row = ttk.Frame(addiction_frame)
    first_row.pack(pady=5)

    global addiction_dropdown
    addiction_dropdown = ttk.OptionMenu(first_row, addiction_var, addiction_options[1], *addiction_options)
    addiction_dropdown.pack(side="left", padx=5)

    global add_addiction_button
    add_addiction_button = ttk.Button(first_row, text="+", command=open_new_addiction_choice)
    add_addiction_button.pack(side="left", padx=5)

    addiction_button.pack()
    back_button_2.pack(pady=5)


def submit_addiction():
    """Einreichen der Sucht"""
    global current_step
    addictions = []
    # Hauptsucht hinzufügen
    if addiction_var.get() != "Bitte auswählen":
        addictions.append(addiction_var.get())

    # Zusätzliche Süchte hinzufügen
    for var, dropdown in additional_addictions:
        if var.get() != "Bitte auswählen":
            addictions.append(var.get())

    if addictions:
        current_step = 3
        user_data["addictions"] = addictions  # Speichere eine Liste aller Süchte
        addiction_label.pack_forget()
        addiction_dropdown.pack_forget()
        add_addiction_button.pack_forget()
        for _, dropdown in additional_addictions:
            dropdown.pack_forget()
        addiction_button.pack_forget()
        back_button_2.pack_forget()
        ask_goal()
    else:
        messagebox.showwarning("Warnung", "Bitte wähle mindestens eine Sucht aus.")


def open_new_addiction_choice():
    """Auswahl weiterer Süchte"""
    new_var = tk.StringVar(root, value="Bitte auswählen")
    new_dropdown = ttk.OptionMenu(addiction_frame, new_var, addiction_options[1], *addiction_options)
    new_dropdown.pack(pady=5)
    additional_addictions.append((new_var, new_dropdown))


def ask_goal():
    """Abfrage vom Ziel"""
    welcome_label.config(text="Super!")
    welcome_label.pack(pady=50)

    goal_label.pack()
    goal_dropdown.pack(pady=10)
    goal_button.pack()
    back_button_3.pack(pady=5)


def submit_goal():
    """Einreichen vom Ziel"""
    global current_step
    user_data["goal"] = goal_var.get()
    if user_data["goal"] != "Bitte auswählen":
        current_step = 4
        goal_label.pack_forget()
        goal_dropdown.pack_forget()
        goal_button.pack_forget()
        back_button_3.pack_forget()
        # Zeigt Widgets der nächsten Abfrage
        ask_sobriety_duration()
    else:
        messagebox.showwarning("Warnung"), "Bitte wähle ein Ziel aus."


def ask_sobriety_duration():
    """Abfrage zur Dauer der nüchternen Zeit"""
    sobriety_label.pack()
    sobriety_date.pack(pady=10)
    sobriety_time_label.pack(pady=10)
    sobriety_hour_dropdown.pack()
    sobriety_minute_dropdown.pack()

    """Lade gespeicherte Sobriety-Duration ins Projekt -falls vorhanden"""
    if "sobriety_date" in user_data:
        sobriety_date.set_date(user_data["sobriety_date"])
    if "sobriety_time" in user_data and ":" in user_data["sobriety_time"]:
        time_parts = user_data["sobriety_time"].split(":")
        if len(time_parts) == 2:
            sobriety_hour.set(time_parts[0])
            sobriety_minute.set(time_parts[1])

    sobriety_button.pack()
    back_button_4.pack(pady=5)


def submit_sobriety_duration():
    """Einreichen der Dauer"""
    global current_step
    raw_date = sobriety_date.get()
    user_data["sobriety_date"] = raw_date

    user_data["sobriety_time"] = f"{sobriety_hour.get()}:{sobriety_minute.get()}"

    if user_data["sobriety_date"] and user_data["sobriety_time"]:
        current_step = 5
        sobriety_label.pack_forget()
        sobriety_date.pack_forget()
        sobriety_time_label.pack_forget()
        sobriety_hour_dropdown.pack_forget()
        sobriety_minute_dropdown.pack_forget()
        sobriety_button.pack_forget()
        back_button_4.pack_forget()

        ask_final_welcome()
    else:
        messagebox.showwarning("Warnung", "Bitte gib ein Datum und eine Zeit an.")


def ask_final_welcome():
    """Willkommenstext nach der kompletten Abfrage"""
    final_welcome_label.pack()
    final_welcome_text.pack()
    final_welcome_button.pack()


def open_main_window():
    """Öffnet das Hauptfenster der Anwendung und schließt root"""
    root.destroy()
    main_window(user_data)


# GUI
root = tk.Tk()
root.title('Willkommen beim Sobriety Tracker!')
root.geometry('600x600')
root.configure()
root.resizable(False, False)

# Mehr Anwenderfreundlichkeit: Returntaste als Alternative zum Klick auf 'weiter'
root.bind('<Return>', on_enter_press)

# Erste Abfrage: Wie heißt du?
welcome_label = ttk.Label(root, text="", font=("Helvetica", 20, "bold"))
name_label = ttk.Label(root, text="Hi! Wie ist dein Name?", font=("Helvetica", 20, "bold"))
name_label.pack(pady=50)

name_entry = ttk.Entry(root)
name_entry.pack(pady=10)
name_entry.focus()  # Cursor landet hiermit direkt im Eingabefeld

name_button = ttk.Button(root, text="Weiter", command=submit_name)
name_button.pack()

# Zweite Abfrage: Sucht
addiction_label = ttk.Label(root, text="Wähle deine Süchte aus:", font=("Helvetica", 13))
addiction_var = tk.StringVar(value="Bitte auswählen")  # Standardwert für das Dropdown
addiction_options = ["Bitte auswählen", "Alkoholsucht", "Nikotinsucht", "Drogensucht", "Internetsucht", "Tablettensucht", "Spielsucht", "Kaufsucht", "Tierische Produkte", "Koffeinsucht", "Andere"]
addiction_button = ttk.Button(root, text="Weiter", command=submit_addiction)
back_button_2 = ttk.Button(root, text="Zurück", command=go_back_to_name)

# Dritte Abfrage: Ziele
goal_label = ttk.Label(root, text="Was möchtest du erreichen?", font=("Helvetica", 13))
goal_var = tk.StringVar(value="Bitte auswählen")
goal_options = ["Weniger Alkohol trinken", "Gesunde Gewohnheiten etablieren", "Rauchen aufgeben", "Nüchtern bleiben", "Bildschirmzeit reduzieren", "Geld sparen", "Mehr Fokus finden", "Andere"]
goal_dropdown = ttk.OptionMenu(root, goal_var, *goal_options)
goal_button = ttk.Button(root, text="Weiter", command=submit_goal)
back_button_3 = ttk.Button(root, text="Zurück", command=go_back_to_addiction)

# Vierte Abfrage
sobriety_label = ttk.Label(root, text="Seit wann bist du nüchtern?", font=("Helvetica", 13))
sobriety_date = DateEntry(root, width=12, borderwidth=2, date_pattern='dd.mm.yy', locale='de_DE')

sobriety_time_label = ttk.Label(root, text="Um welche Uhrzeit?", font=("Helvetica", 13))

sobriety_hour = tk.StringVar(value="00")
sobriety_hour_dropdown = ttk.OptionMenu(root, sobriety_hour, "00", *[f"{i:02}" for i in range(24)])

sobriety_minute = tk.StringVar(value="00")
sobriety_minute_dropdown = ttk.OptionMenu(root, sobriety_minute, "00",*[f"{i:02}" for i in range(60)])

sobriety_button = ttk.Button(root, text="Weiter", command=submit_sobriety_duration)
back_button_4 = ttk.Button(root, text="Zurück", command=go_back_to_goal)


# Fünfte "Abfrage", eher das finale Welcome Window:
final_welcome_label = ttk.Label(root, text="** Willkommen auf deiner Sobriety-Reise **", font=("Helvetica", 13, "bold"), justify="center")
final_welcome_text = ttk.Label(root,
                               text="Fertig! Sehen wir uns jetzt deinen Tracker an. " 
                                          "Hier kannst du deine nüchternen Tage verfolgen und deine Erfolge feiern!",
                               font=("Helvetica", 13),
                               justify="center",
                               wraplength=500)
final_welcome_button = ttk.Button(root, text="Weiter", command=open_main_window)


root.mainloop()