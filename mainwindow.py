import tkinter as tk
from datetime import datetime
from tkinter import ttk
import webbrowser


def main_window(user_data):
    """Erstellt das Hauptfenster der Sobriety-Tracker-Anwendung mit Live-Timer."""

    def apply_theme(dark_mode):
        if dark_mode:
            bg = "#2e2e2e"
            fg = "white"
            style.configure("TLabel", background=bg, foreground=fg)
            style.configure("TButton", background=bg, foreground=fg)
            style.configure("TCheckbutton", background=bg, foreground=fg)
            window2.configure(background=bg)
        else:
            bg = "SystemButtonFace"
            fg = "black"
            style.configure("TLabel", background=bg, foreground=fg)
            style.configure("TButton", background=bg, foreground=fg)
            style.configure("TCheckbutton", background=bg, foreground=fg)
            window2.configure(background=bg)

    def open_settings():
        settings_window = tk.Toplevel()
        settings_window.title("Einstellungen")
        settings_window.geometry("300x150")

        is_dark_mode = tk.BooleanVar(value=user_data.get("dark_mode", False))

        def toggle_theme():
            dark = is_dark_mode.get()
            user_data["dark_mode"] = dark
            apply_theme(dark)

        dark_mode_check = ttk.Checkbutton(
            settings_window,
            text="Dark Mode aktivieren",
            variable=is_dark_mode,
            command=toggle_theme
        )
        dark_mode_check.pack(pady=40)

    def open_help():
        help_window = tk.Toplevel()
        help_window.title("Hilfe")
        help_window.geometry("600x600")

        content_frame = tk.Frame(help_window)
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)

        def add_label(master, text, size=12, pady=2, bold=False):
            font = ("Helvetica", size, "bold") if bold else ("Helvetica", size)
            label = tk.Label(master, text=text, font=font, anchor='w', justify='left')
            label.pack(anchor='w', pady=pady, fill='x')
            return label

        add_label(content_frame, "Hier findest du Hilfe in Notsituationen:", size=16, bold=True, pady=(0, 10))

        add_label(content_frame, "Notrufnummern:", size=14, bold=True, pady=(10, 5))
        add_label(content_frame, "Polizeinotruf: 110")
        add_label(content_frame, "Feuerwehr und Notruf: 112")
        add_label(content_frame, "Ärztlicher Bereitschaftsdienst: 116 117")

        add_label(content_frame, "Seelsorge und Telefonberatung:", size=14, bold=True, pady=(15, 5))
        add_label(content_frame, "TelefonSeelsorge: 116 123 oder 0800 1110111 / 0800 1110222")
        add_label(content_frame, "Ärztlicher Bereitschaftsdienst: 116 117")
        add_label(content_frame, "Sucht & Drogenhotline: 01806 313031")
        add_label(content_frame, "Infotelefon zur Suchtvorbeugung: 0221 89 20 31")
        add_label(content_frame, "Telefonberatung zur Rauchentwöhnung: 0800 8 31 31 31")
        add_label(content_frame, "Telefonberatung zur Glücksspielsucht: 0800 1 37 27 00")

        add_label(content_frame, "Weitere Hilfeseiten:", size=14, bold=True, pady=(15, 5))

        button_frame = tk.Frame(content_frame)
        button_frame.pack(anchor='w', fill='x')

        websites = [
            ("Der Beauftragte der Bundesregierung für Sucht- und Drogenfragen",
             "https://www.bundesdrogenbeauftragter.de/service/beratungsangebote/"),
            ("Deutsches Rotes Kreuz Suchtberatung:",
             "https://www.drk.de/hilfe-in-deutschland/gesundheit-und-praevention/suchtberatung/"),
            ("DHS Deutsche Hauptstelle für Suchtfragen e.V.", "https://www.dhs.de/")
        ]

        max_width = 60

        for text, url in websites:
            btn = tk.Button(button_frame, text=text, anchor='w', width=max_width,
                            command=lambda link=url: webbrowser.open(link))
            btn.pack(anchor='w', pady=5)


    def open_challenge():
        challenge_window = tk.Toplevel()
        challenge_window.title("Challenges")
        challenge_window.geometry("400x400")

        canvas = tk.Canvas(challenge_window, width=400, height=400, highlightthickness=0)
        canvas.pack()

        today = datetime.now()
        sobriety_date_str = user_data.get('sobriety_date', 'unbekannt')
        sobriety_time_str = user_data.get('sobriety_time', '00:00')

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
                label = tk.Label(challenge_window, text=text, font=("Helvetica", 12, "bold"), fg="green")
                label.place(x=20, y=y_pos)
                canvas.create_text(250, y_pos + 20, text="🎉🎉🎉", font=("Helvetica", 18))
            else:
                label = tk.Label(challenge_window, text=f"🔒 Freigeschaltet bei {day} Tagen", font=("Helvetica", 12),
                                 fg="grey")
                label.place(x=20, y=y_pos)
            y_pos += 60

    def open_goals():
        goal_window = tk.Toplevel()
        goal_window.title("Ziele")
        goal_window.geometry("400x400")
        goal_window.configure()

        if "notes" not in user_data:
            user_data["notes"] = []

        def safe_note():
            """Speichert eine neue Notiz mit Datum und aktualisiert die Anzeige."""
            note_text = free_text_entry.get().strip()
            if note_text:  # Falls das Feld nicht leer ist
                today = datetime.now().strftime("%d.%m.%Y")  # Heutiges Datum als String
                user_data["notes"].insert(0, f"{today}: {note_text}")  # Neuen Eintrag oben einfügen
                free_text_entry.delete(0, tk.END)  # Löscht das Eingabefeld nach dem Speichern
                update_notes_display()  # Aktualisiert die Anzeige

        def update_notes_display():
            """Aktualisiert die Anzeige der gespeicherten Notizen."""
            note_label.config(text="\n".join(user_data["notes"]))  # Notizen untereinander anzeigen

        goal_label = ttk.Label(goal_window, text=f"Dein Ziel: {user_data['goal']}!", font=("Helvetica", 16))
        goal_label.pack()
        free_text_label = ttk.Label(goal_window, text="Hier ist Platz für Notizen und Gedanken.", font=("Helvetica", 14))
        free_text_label.pack()
        free_text_entry = ttk.Entry(goal_window, width=70, font=("Helvetica", 14))
        free_text_entry.pack(pady=10)
        free_text_button = ttk.Button(goal_window, text="Speichern", command=safe_note)
        free_text_button.place(x=300, y=90)
        note_label = ttk.Label(goal_window, text="", font=("Helvetica", 12), justify="left", anchor="w")
        note_label.place(x=20, y=110)

        update_notes_display()

    def update_timer():
        """Berechnet die Differenz zwischen dem Nüchternheitsdatum und jetzt und aktualisiert die Anzeige."""
        today = datetime.now()  # Aktuelle Zeit
        sobriety_date_str = user_data.get('sobriety_date', 'unbekannt')  # Im Format "06.01.25"
        sobriety_time_str = user_data.get('sobriety_time', '00:00')  # Im Format "HH:MM"

        sobriety_datetime = datetime.strptime(f"{sobriety_date_str} {sobriety_time_str}", "%d.%m.%y %H:%M")

        delta = today - sobriety_datetime
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        canvas.itemconfig(time_texts[0], text=f"{days:02}")
        canvas.itemconfig(time_texts[1], text=f"{hours:02}")
        canvas.itemconfig(time_texts[2], text=f"{minutes:02}")
        canvas.itemconfig(time_texts[3], text=f"{seconds:02}")

        progress_angle = (hours / 24) * 360  # Berechnung des Winkels
        canvas.itemconfig(progress_arc, extent=-progress_angle)

        window2.after(1000, update_timer)

    window2 = tk.Tk()
    window2.title('Sobriety Tracker')
    window2.geometry('600x600')
    window2.configure()
    window2.resizable(False, False)
    # style
    style = ttk.Style()
    style.theme_use('alt')


    settings_button = ttk.Button(window2, text='Settings', command=open_settings)
    settings_button.place(x=20, y=20)

    label = ttk.Label(window2, text=f"Willkommen beim Sobriety Tracker, {user_data['name']}!", font=("Helvetica", 16))
    label.pack(pady=20)

    canvas = tk.Canvas(window2, width=400, height=400, highlightthickness=0)
    canvas.pack()

    canvas.create_oval(50, 50, 350, 350, outline="grey", width=3)

    rect_positions = [(90, 170), (150, 170), (210, 170), (270, 170)]
    rects = []
    for x, y in rect_positions:
        rects.append(canvas.create_rectangle(x, y, x+50, y+50, outline="lavender", width=2, fill="white"))

    time_texts = [
        canvas.create_text(115, 195, text="00", font=("Helvetica", 14, "bold")),
        canvas.create_text(175, 195, text="00", font=("Helvetica", 14, "bold")),
        canvas.create_text(235, 195, text="00", font=("Helvetica", 14, "bold")),
        canvas.create_text(295, 195, text="00", font=("Helvetica", 14, "bold"))
    ]
    labels = ["Tage", "Stunden", "Minuten", "Sekunden"]
    for i, label_text in enumerate(labels):
        canvas.create_text(115 + (i * 60), 245, text=label_text, font=("Helvetica", 10))

    for i in range(3):
        canvas.create_text(145 + (i * 60), 195, text=":", font=("Helvetica", 14, "bold"))

    progress_arc = canvas.create_arc(50, 50, 350, 350, start=90, extent=0, outline="SkyBlue1", width=5, style="arc")


    help_button = ttk.Button(window2, text='Hilfe', command=open_help)
    help_button.place(x=20, y=550)

    challenge_button = ttk.Button(window2, text="Challenges", command=open_challenge)
    challenge_button.place(x=250, y=550)

    goals_button = ttk.Button(window2, text="Ziele", command=open_goals)
    goals_button.place(x=500, y=550)

    update_timer()

    window2.mainloop()


