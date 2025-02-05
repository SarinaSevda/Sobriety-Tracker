import tkinter as tk
from datetime import datetime


def main_window(user_data):
    """Erstellt das Hauptfenster der Sobriety-Tracker-Anwendung mit Live-Timer."""
#    window2 = tk.Tk()
#    window2.title('Sobriety Tracker')
#    window2.geometry('600x600')
#    window2.configure(bg='white')
#    window2.resizable(False, False)
#
#    label = tk.Label(window2, text="Willkommen im Sobriety Tracker!", font=("Helvetica", 16))
#    label.pack(pady=20)
#
#    timer_label = tk.Label(window2, text="", font=("Helvetica", 14), fg="green")
#    timer_label.pack(pady=20)

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

        timer_label.config(
            text=f"Nüchtern seit: {days} Tage, {hours} Stunden, {minutes} Minuten, {seconds} Sekunden"
        )

        window2.after(1000, update_timer)

    window2 = tk.Tk()
    window2.title('Sobriety Tracker')
    window2.geometry('600x600')
    window2.configure(bg='white')
    window2.resizable(False, False)

    settings_button = tk.Button(window2, text='Settings', command=open_settings)
    settings_button.pack()

    label = tk.Label(window2, text="Willkommen im Sobriety Tracker!", font=("Helvetica", 16))
    label.pack(pady=20)

    timer_label = tk.Label(window2, text="", font=("Helvetica", 14), fg="green")
    timer_label.pack(pady=20)

    help_button = tk.Button(window2, text='Hilfe', command=open_help)
    help_button.pack()

    challenge_button = tk.Button(window2, text="Challenges", command=open_challenge)
    challenge_button.pack()

    goals_button = tk.Button(window2, text="Ziele", command=open_goals)
    goals_button.pack()

    update_timer()

    window2.mainloop()
