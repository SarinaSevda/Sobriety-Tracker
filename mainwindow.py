import tkinter as tk
from datetime import datetime

def main_window(user_data):
    """Erstellt das Hauptfenster der Sobriety-Tracker-Anwendung mit Live-Timer."""
    window2 = tk.Tk()
    window2.title('Sobriety Tracker')
    window2.geometry('600x600')

    label = tk.Label(window2, text="Willkommen im Sobriety Tracker!", font=("Helvetica", 16))
    label.pack(pady=20)

    timer_label = tk.Label(window2, text="", font=("Helvetica", 14), fg="green")
    timer_label.pack(pady=20)

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

    update_timer()

    window2.mainloop()
