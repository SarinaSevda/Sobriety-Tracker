# ersetzt das bisherige mainwindow.py: GUI-Logik, -aufbau und -steuerung der Nutzerdatenerfassung


import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox  # **neue Referenz für GUI-Aufbau
from styles import *
from user_model import UserData  # **neue referenz
from main_application import MainApplication

# Optionen für Süchte
ADDICTION_OPTIONS = [
    "Alkoholsucht",
    "Nikotinsucht",
    "Koffeinsucht",
    "Drogensucht",
    "Internetsucht",
    "Tablettensucht",
    "Spielsucht",
    "Kaufsucht",
    "Tierische Produkte",
    "Andere"
]

# Optionen für Ziele
GOAL_OPTIONS = [
    "Weniger Alkohol trinken", "Gesunde Gewohnheiten etablieren",
    "Rauchen aufgeben", "Nüchtern bleiben",
    "Bildschirmzeit reduzieren", "Geld sparen",
    "Mehr Fokus finden", "Etwas anderes"
]


class Gui_Wizard:  # ******NEU*******
    def __init__(self, root, user_data: UserData):
        self.root = root
        self.user_data = UserData()
        self.additional_addictions = []

        # Style anwenden
        configure_styles()

        # legt Widgets an, ohne sie direkt anzuzeigen. Werden unten dann aufgerufen.

        self.welcome_label = ttk.Label(
            root, text="", **NAME_LABEL_STYLE)  # Allgemeines Willkommen

        # Schritt 1: Name
        # **warum hier root und unten self.root?
        self.name_label = ttk.Label(
            root, text="Wie ist dein Name?", **NAME_LABEL_STYLE)
        self.name_button = ttk.Button(
            root, text="Weiter", command=self.submit_name)
        self.name_entry = ttk.Entry(root)

        # Schritt 2: Sucht
        self.addiction_label = ttk.Label(
            root, text="Wähle deine Süchte aus:", **ADDICTION_LABEL_STYLE)
        self.addiction_var = tk.StringVar(root, value="Bitte auswählen")
        self.addiction_frame = ttk.Frame(root)

        self.first_row = ttk.Frame(self.addiction_frame)
        self.first_row.pack()

        self.addiction_dropdown = ttk.OptionMenu(
            self.addiction_frame,
            self.addiction_var,
            ADDICTION_OPTIONS[1],
            *ADDICTION_OPTIONS
        )

        self.add_addiction_button = ttk.Button(
            self.addiction_frame,
            text="+",
            command=self.open_new_addiction_choice
        )

        self.addiction_button = ttk.Button(
            root,
            text="Weiter",
            command=self.submit_addiction
        )

        self.back_button_2 = ttk.Button(
            root,
            text="Zurück",
            command=self.ask_name
        )

        # Schritt 3: Ziele
        self.goal_label = ttk.Label(
            self.root, text="Was möchtest du erreichen?", **GOAL_LABEL_STYLE)
        self.goal_var = tk.StringVar(value="Bitte auswählen")
        self.goal_dropdown = ttk.OptionMenu(
            self.root, self.goal_var, *GOAL_OPTIONS)
        self.goal_button = ttk.Button(
            self.root, text="Weiter", command=self.submit_goal)
        self.back_button_3 = ttk.Button(
            self.root, text="Zurück", command=self.ask_addiction)

        # Schritt 4: Startzeitpunkt
        self.sobriety_label = ttk.Label(
            self.root, text="Seit wann bist du nüchtern?", **SOBRIETY_LABEL_STYLE)
        self.sobriety_date = DateEntry(
            self.root, width=12, borderwidth=2, date_pattern='dd.mm.yy', locale='de_DE')

        self.sobriety_time_label = ttk.Label(
            self.root, text="Super! Um welche Uhrzeit?", **SOBRIETY_LABEL_STYLE)
        self.sobriety_hour = tk.StringVar(value="00")
        self.sobriety_hour_dropdown = ttk.OptionMenu(self.root, self.sobriety_hour, "00",
                                                     *[f"{i:02}" for i in range(24)])

        self.sobriety_minute = tk.StringVar(value="00")
        self.sobriety_minute_dropdown = ttk.OptionMenu(self.root, self.sobriety_minute, "00",
                                                       *[f"{i:02}" for i in range(60)])

        self.sobriety_button = ttk.Button(
            self.root, text="Weiter", command=self.submit_sobriety_duration)
        self.back_button_4 = ttk.Button(
            self.root, text="Zurück", command=self.ask_goal)

        # Schritt 5: Abschluss
        self.final_welcome_label = ttk.Label(self.root, text="Willkommen auf deiner Sobriety-Reise",
                                             **WELCOME_LABEL_STYLE)
        self.final_welcome_text = ttk.Label(self.root,
                                            text="Fertig! Sehen wir uns jetzt deinen Tracker an.\nHier kannst du deine nüchternen Tage verfolgen und deine Erfolge feiern!",
                                            **FINAL_LABEL_STYLE)
        self.final_welcome_button = ttk.Button(self.root, text="Weiter",
                                               command=self.open_main_window
                                               )

        self.ask_name()  # startet Schritt1

    # Funktionen (nur Abfragemaske)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def open_main_window(self):
        self.user_data.save_to_db()  # Nutzerdaten speichern
        self.root.destroy()  # GUI-Fenster schließen
        new_root = tk.Tk()
        MainApplication(new_root, self.user_data)
        new_root.mainloop()

    def ask_name(self):

        self.clear_screen()
        self.welcome_label.config(text="Willkommen!")
        self.welcome_label.pack(pady=50)

        self.name_label.pack()
        self.name_entry.pack(pady=10)
        self.name_entry.focus()  # Cursor landet hiermit direkt im Eingabefeld

        self.name_button.pack()

    def submit_name(self):
        name = self.name_entry.get()
        if name:
            self.user_data.name = name
            self.user_data.load_from_db()
            self.ask_addiction()
        else:
            messagebox.showwarning("Warnung", "Bitte gib deinen Namen ein.")

    def ask_addiction(self):

        self.clear_screen()
        self.welcome_label.config(text=f"Willkommen, {self.user_data.name}!\nBitte wähle deine Süchte aus.", wraplength=500,
                                  justify="center")
        self.welcome_label.pack(pady=50)

        self.addiction_label.pack()
        self.addiction_frame.pack(pady=10)
        self.first_row.pack(pady=5)

        self.addiction_button.pack(padx=5)
        self.add_addiction_button.pack(side="left", padx=5)

        self.addiction_button.pack(pady=10)
        self.back_button_2.pack(pady=5)

    def open_new_addiction_choice(self):
        new_var = tk.StringVar(self.root, value=ADDICTION_OPTIONS[0])
        new_dropdown = ttk.OptionMenu(
            self.addiction_frame, new_var, ADDICTION_OPTIONS[0], *ADDICTION_OPTIONS)
        new_dropdown.pack(pady=5)
        self.additional_addictions.append((new_var, new_dropdown))

    def submit_addiction(self):
        addictions = []
        if self.addiction_var.get() != "Bitte auswählen":
            addictions.append(self.addiction_var.get())
        for var, _ in self.additional_addictions:
            if var.get() != "Bitte auswählen":
                addictions.append(var.get())

        if addictions:
            self.user_data.addictions = addictions
            self.ask_goal()
        else:
            messagebox.showwarning("Warnung", "Bitte gib eine Sucht ein.")

    def ask_goal(self):

        self.clear_screen()
        self.welcome_label.config(text="Super!")
        self.welcome_label.pack(pady=50)

        self.goal_label.pack(padx=5)
        self.goal_dropdown.pack(padx=10)
        self.goal_button.pack(pady=10)
        self.back_button_3.pack(pady=5)

    def submit_goal(self):
        goal = self.goal_var.get()
        if goal:
            self.user_data.goal = goal
            self.ask_sobriety()
        else:
            messagebox.showwarning("Warnung", "Bitte wähle ein Ziel aus.")

    def ask_sobriety(self):

        self.clear_screen()
        self.sobriety_label.pack(pady=50)

        self.sobriety_date.pack(pady=5)

        self.sobriety_time_label.pack(pady=60)
        self.sobriety_hour_dropdown.pack(padx=5)
        self.sobriety_minute_dropdown.pack(padx=5)

        self.sobriety_button.pack(pady=10)
        self.back_button_4.pack(pady=5)

    def submit_sobriety_duration(self):
        self.user_data.sobriety_date = self.sobriety_date.get()
        self.user_data.sobriety_time = f"{self.sobriety_hour.get()}:{self.sobriety_minute.get()}"
        self.show_final_screen()

    def show_final_screen(self):
        self.clear_screen()
        self.final_welcome_label.pack(pady=50)
        self.final_welcome_text.pack(pady=10)
        self.final_welcome_button.pack(pady=30)
