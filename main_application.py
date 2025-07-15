import tkinter as tk
from tkinter import ttk
from user_model import UserData
from styles import *
import webbrowser
import random
from datetime import datetime

#Zitatoptionen
QUOTES_OPTIONS = [
    "Ein Tag nach dem anderen.",
    "Du bist stärker als du denkst.",
    "Heute zählt. Bleib dran!",
    "Stolz beginnt mit einem Schritt.",
    "Kleine Schritte – große Wirkung.",
    "Heute wird ein guter Tag!"
]



class MainApplication:
    def __init__(self, root, user_data):
        self.root = root
        self.root.title("Dein Sobriety Tracker")
        self.root.geometry("600x600")
        self.root.update_idletasks()
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        size = tuple(int(_) for _ in self.root.geometry().split("+")[0].split("x"))
        x = w // 2 - size[0] // 2
        y = h // 2 - size[1] // 2
        self.root.geometry(f"{size[0]}x{size[1]}+{x}+{y}")
        self.root.resizable(False, False)

        self.user_data = user_data

        # Style anwenden
        self.dark_mode = False
        apply_theme(ttk.Style(), self.dark_mode, self.root)

        # Haupt-Frame anlegen
        self.main_frame = ttk.Frame(self.root)

        # Settings-Button
        self.settings_button = ttk.Button(self.main_frame,text="", command=self.open_settings)
        self.settings_label = ttk.Label(self.main_frame,text="", **SETTINGS_LABEL_STYLE)

        # Quotes
        self.quote_label = ttk.Label(self.main_frame, text="", **QUOTE_LABEL_STYLE)

        # Hilfe-Labels
        self.help_label_heading = ttk.Label(self.root, text="",
                                            **HELP_LABEL_STYLE["bold"])  # heading
        self.help_label_normal = ttk.Label(self.root, text="",
                                           **HELP_LABEL_STYLE["normal"])  # z.B. für einzelne Notrufzeilen

        #Interface aufbauen
        self.build_main_interface()

        # Timer initialisieren
        self.init_timer_canvas()
        self.update_timer()


    def build_main_interface(self):
        self.main_frame.pack(fill="both", expand=True)

        #Buttons
        # Einstellungen-Button
        self.settings_button.config(text="Einstellungen")
        self.settings_button.place(x=20, y=20)

        self.settings_label.config(text=f"Hi, {self.user_data.get('name')}!")
        self.settings_label.place(x=300, y=35, anchor="center")

        # Challenge-Button
        challenge_button = ttk.Button(self.main_frame, text="Meine Erfolge", command=self.open_challenge)
        challenge_button.place(x=250, y=550)

        #Hilfe-Button
        help_button = ttk.Button(self.main_frame, text='Hilfe', command=self.open_help)
        help_button.place(x=20, y=550)

        #Ziele-u-Reflektion-Button
        goalrefl_button = ttk.Button(self.main_frame, text="Ziele & Reflektion", command=self.open_goalrefl)
        goalrefl_button.place(x=480, y=550)

        #zufällige Zitatauswahl
        selected_quote = random.choice(QUOTES_OPTIONS)
        self.quote_label.config(text=selected_quote)
        self.quote_label.place(x=300, y=90, anchor="center")


    #Einstellungen mit Theme-Anpassung
    def apply_theme_to_app(self, dark_mode):  # wendet Dark Mode an
        apply_theme(ttk.Style(), dark_mode, self.root)

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Einstellungen")
        settings_window.geometry("300x150")

        is_dark_mode = tk.BooleanVar(value=self.dark_mode)

        def toggle_theme():
            self.dark_mode = is_dark_mode.get()
            self.apply_theme_to_app(self.dark_mode)  # Theme anwenden

        dark_mode_check = ttk.Checkbutton(
            settings_window,
            text="Dark-Mode aktivieren",
            variable=is_dark_mode,
            command=toggle_theme
        )
        dark_mode_check.pack(pady=40)

        self.apply_theme_to_app(is_dark_mode.get())

    def open_help(self):  # ***fertig
        self.help_window = tk.Toplevel(self.root)
        self.help_window.title("Hilfe")
        self.help_window.geometry("600x600")

        help_frame = tk.Frame(self.help_window)
        help_frame.pack(fill='both', expand=True, padx=20, pady=20)

        help_label(help_frame, "Hier findest du Hilfe in Notsituationen:",
                   style=HELP_LABEL_STYLE["bold"], pady=(0, 10))

        help_label(help_frame, "Notrufnummern",
                   style=HELP_LABEL_STYLE["bold"], pady=(10, 5))

        help_label(help_frame, "Polizeinotruf: 110",
                   style=HELP_LABEL_STYLE["normal"])
        help_label(help_frame, "Feuerwehr und Notruf: 112",
                   style=HELP_LABEL_STYLE["normal"])
        help_label(help_frame, "Ärztlicher Bereitschaftsdienst: 116 117",
                   style=HELP_LABEL_STYLE["normal"])

        help_label(help_frame, "Seelsorge und Beratung",
                   style=HELP_LABEL_STYLE["bold"], pady=(15, 5))
        help_label(help_frame, "Ärztlicher Bereitschaftsdienst: 116 117",
                   style=HELP_LABEL_STYLE["normal"])
        help_label(help_frame, "Telefonseelsorge: 116 123 oder 0800 1110111 / 0800 1110222",
                   style=HELP_LABEL_STYLE["normal"])
        help_label(help_frame, "Sucht & Drogenhotline: 01806 313031",
                   style=HELP_LABEL_STYLE["normal"])
        help_label(help_frame, "Infotelefon zur Suchtvorbeugung: 0221 89 20 31",
                   style=HELP_LABEL_STYLE["normal"])
        help_label(help_frame, "Telefonberatung zur Glücksspielsucht: 0800 1 37 27 00",
                   style=HELP_LABEL_STYLE["normal"])
        help_label(help_frame, "Telefonberatung zur Rauchentwöhnung: 0800 8 31 31 31",
                   style=HELP_LABEL_STYLE["normal"])

        help_label(help_frame, "Weitere Hilfeseiten:", style= HELP_LABEL_STYLE["bold"], pady=(15, 5))

        websites = [
            ("Bundesdrogenbeauftragter", "https://www.bundesdrogenbeauftragter.de/service/beratungsangebote/"),
            ("DRK Suchtberatung", "https://www.drk.de/hilfe-in-deutschland/gesundheit-und-praevention/suchtberatung/"),
            ("DHS Hauptstelle für Suchtfragen", "https://www.dhs.de/")
        ]

        # Links anzeigen
        for text, url in websites:
            link = tk.Label(help_frame, text=text, fg="blue", cursor="hand2", underline=True)
            link.pack(anchor="w", pady=2)
            link.bind("<Button-1>", lambda e, link_url=url: webbrowser.open(link_url))


        apply_theme(ttk.Style(), self.dark_mode, self.help_window)


    def open_challenge(self):
        challenge_window = tk.Toplevel(self.root)
        challenge_window.title("Challenges")
        challenge_window.geometry("400x400")

        canvas = tk.Canvas(challenge_window, width=400, height=400, highlightthickness=0)
        canvas.pack()

        today = datetime.now()
        sobriety_date_str = self.user_data.get('sobriety_date', 'unbekannt')
        sobriety_time_str = self.user_data.get('sobriety_time', '00:00')

        try:
            sobriety_datetime = datetime.strptime(f"{sobriety_date_str} {sobriety_time_str}", "%d.%m.%y %H:%M")
            days_sober = (today - sobriety_datetime).days
        except Exception:
            days_sober = 0

        milestones = [
            (10, "🥉 10 Tage – Bronze-Medaille!"),
            (30, "🥈 1 Monat – Silber-Medaille!"),
            (100, "🥇 100 Tage – Gold-Medaille!"),
            (365, "🏅 1 Jahr – Held:innen-Medaille!")
        ]

        y_pos = 20
        for day, text in milestones:
            if days_sober >= day:
                label = ttk.Label(challenge_window, text=text, **CHALLENGE_LABEL_UNLOCKED)
                label.place(x=20, y=y_pos)
                canvas.create_text(250, y_pos + 20, text="🎉🎉🎉", **CHALLENGE_LABEL_UNLOCKED)
            else:
                label = ttk.Label(challenge_window, text=f"🔒 Freigeschaltet bei {day} Tagen",
                                 **CHALLENGE_LABEL_LOCKED)
                label.place(x=20, y=y_pos)
            y_pos += 60

        apply_theme(ttk.Style(), self.dark_mode, challenge_window)

    #Ziele und Reflektion
    def open_goalrefl(self):
        self.goalrefl_window = tk.Toplevel(self.root)
        self.goalrefl_window.title("Ziele und Reflektion")
        self.goalrefl_window.geometry("400x400")

        apply_theme(ttk.Style(), self.dark_mode, self.goalrefl_window)


        #Ziel anzeigen
        goalrefl_text = f"Dein Ziel: {self.user_data.get('goal')}!"
        goalrefl_label = ttk.Label(self.goalrefl_window, text=goalrefl_text, **REFLECTION_LABEL_STYLE)
        goalrefl_label.pack(pady=(10, 5))

        # Notizfeld
        free_text_label = ttk.Label(self.goalrefl_window, text="Platz für deine Gedanken:", **REFLECTION_LABEL_STYLE)
        free_text_label.pack()

        self.free_text_entry = ttk.Entry(self.goalrefl_window, width=50, **TEXT_ENTRY_STYLE)
        self.free_text_entry.pack(pady=5)

        save_button = ttk.Button(self.goalrefl_window, text="Speichern", command=self.save_note)
        save_button.pack(pady=(0, 10))

        # Scrollbarer Notizbereich
        note_frame = ttk.Frame(self.goalrefl_window)
        note_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.note_text_widget = tk.Text(note_frame, wrap="word", height=10, **NOTE_TEXT_STYLE)
        self.note_text_widget.pack(side="left", fill="both", expand=True)

        if self.dark_mode:
            self.note_text_widget.config(bg="#444444", fg="white", insertbackground="white")
        else:
            self.note_text_widget.config(bg="white", fg="black", insertbackground="black")

        scrollbar = ttk.Scrollbar(note_frame, command=self.note_text_widget.yview)
        scrollbar.pack(side="right", fill="y")

        self.note_text_widget.config(yscrollcommand=scrollbar.set, state="disabled")

        self.update_notes_display()

    def save_note(self):
        note_text = self.free_text_entry.get().strip()
        if note_text:
            today = datetime.now().strftime("%d.%m.%Y")
            full_note = f"{today}: {note_text}"
            self.user_data.note.insert(0, full_note)
            self.free_text_entry.delete(0, tk.END)
            self.update_notes_display()

    def update_notes_display(self):
        notes = self.user_data.note
        self.note_text_widget.config(state="normal")
        self.note_text_widget.delete("1.0", tk.END)
        self.note_text_widget.insert(tk.END, "\n\n".join(notes))
        self.note_text_widget.config(state="disabled")


    def init_timer_canvas(self):   #Timer-Gui (ausgelagerter Teil von build_main_interface)
        self.canvas = tk.Canvas(self.main_frame, width=400, height=400, highlightthickness=0)
        self.canvas.place(x=105, y=105)

        #Kreis
        self.canvas.create_oval(50, 50, 350, 350, **TIMER_OVAL_STYLE)

        #Rechtecke
        rect_positions = [(90, 170), (150, 170), (210, 170), (270, 170)]
        self.rects = []
        for x, y in rect_positions:
            self.rects.append(
                self.canvas.create_rectangle(x,y, x+50, y+50, **TIMER_RECT_STYLE)
            )

        self.time_texts = [
            self.canvas.create_text(115, 195, text="00", **TIMER_TEXT_STYLE),
            self.canvas.create_text(175, 195, text="00", **TIMER_TEXT_STYLE),
            self.canvas.create_text(235, 195, text="00", **TIMER_TEXT_STYLE),
            self.canvas.create_text(295, 195, text="00", **TIMER_TEXT_STYLE)
        ]
        labels = ["Tage", "Stunden", "Minuten", "Sekunden"]
        label_positions = [(115, 230), (175, 230), (235, 230), (295, 230)]
        for (x, y), text in zip(label_positions, labels):
            self.canvas.create_text(x, y, text=text, **DATENTIME_LABEL_STYLE)

        self.progress_arc = self.canvas.create_arc(
            50, 50, 350, 350,
            start=90, extent=0,
            outline="SkyBlue1", width=5, style="arc"
        )

    def get_sobriety_datetime(self):
        try:
            date_str = self.user_data.get("sobriety_date", "")
            time_str = self.user_data.get("sobriety_time", "00:00")
            return datetime.strptime(f"{date_str} {time_str}", "%d.%m.%y %H:%M")
        except Exception:
            return datetime.now()

    def update_timer(self):
        now = datetime.now()
        sobriety_dt = self.get_sobriety_datetime()
        delta = now - sobriety_dt

        days = delta.days
        hours, rem = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        for i, value in enumerate([days, hours, minutes, seconds]):
            self.canvas.itemconfig(self.time_texts[i], text=f"{value:02}")

        progress_angle = (hours / 24) * 360
        self.canvas.itemconfig(self.progress_arc, extent=-progress_angle)

        self.root.after(1000, self.update_timer)







