import tkinter as tk
from datetime import datetime


def main_window(user_data):
    """Erstellt das Hauptfenster der Sobriety-Tracker-Anwendung mit Live-Timer."""
    def open_settings():
        settings_window = tk.Toplevel()
        settings_window.title("Einstellungen")

    def open_help():
        help_window = tk.Toplevel()
        help_window.title("Hilfe")

    def open_challenge():
        challenge_window = tk.Toplevel()
        challenge_window.title("Challenges")

    def open_goals():
        goal_window = tk.Toplevel()
        goal_window.title("Ziele")


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
    window2.configure(bg='white')
    window2.resizable(False, False)

    settings_button = tk.Button(window2, text='Settings', command=open_settings)
    settings_button.pack()

    label = tk.Label(window2, text=f"Willkommen beim Sobriety Tracker, {user_data['name']}!", font=("Helvetica", 16))
    label.pack(pady=20)

    canvas = tk.Canvas(window2, width=400, height=400, bg="white", highlightthickness=0)
    canvas.pack()

    canvas.create_oval(50, 50, 350, 350, outline="black", width=3)

    rect_positions = [(120, 180), (180, 180), (240, 180), (300, 180)]
    rects = []
    for x, y in rect_positions:
        rects.append(canvas.create_rectangle(x, y, x+50, y+50, outline="black", width=2, fill="white"))

    time_texts = [
        canvas.create_text(145, 205, text="00", font=("Helvetica", 14, "bold")),
        canvas.create_text(205, 205, text="00", font=("Helvetica", 14, "bold")),
        canvas.create_text(265, 205, text="00", font=("Helvetica", 14, "bold")),
        canvas.create_text(325, 205, text="00", font=("Helvetica", 14, "bold"))
    ]
    labels = ["Tage", "Stunden", "Minuten", "Sekunden"]
    for i, label_text in enumerate(labels):
        canvas.create_text(145 + (i * 60), 230, text=label_text, font=("Helvetica", 10))

    for i in range(3):
        canvas.create_text(175 + (i * 60), 205, text=":", font=("Helvetica", 14, "bold"))

    progress_arc = canvas.create_arc(50, 50, 350, 350, start=90, extent=0, outline="blue", width=5, style="arc")


    help_button = tk.Button(window2, text='Hilfe', command=open_help)
    help_button.pack()

    challenge_button = tk.Button(window2, text="Challenges", command=open_challenge)
    challenge_button.pack()

    goals_button = tk.Button(window2, text="Ziele", command=open_goals)
    goals_button.pack()

    update_timer()

    window2.mainloop()
