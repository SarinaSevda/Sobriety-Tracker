import tkinter as tk
from datetime import datetime

def main_window(user_data):
    """Erstellt das Hauptfenster der Sobriety-Tracker-Anwendung."""
    window2 = tk.Toplevel()
    window2.title('Sobriety Tracker')
    window2.geometry('600x600')

    label = tk.Label(window2, text="Willkommen im Sobriety Tracker!", font=("Helvetica", 16))
    label.pack(pady=20)

    def show_sobriety_duration():
        today = datetime.now()
        sobriety_date_str = user_data.get('sobriety_date', 'unbekannt')  # Z. B. '06.01.25'
        sobriety_datetime = datetime.strptime(sobriety_date_str, "%d.%m.%y")
        days_sober = (today - sobriety_datetime).days

        label2 = tk.Label(
            window2,
            text=f"Nüchtern seit: {sobriety_date_str}.",
            font=("Helvetica", 14)
        )
        label2.pack(pady=10)

        label3 = tk.Label(
            window2,
            text=f"Du bist seit {days_sober} Tagen nüchtern.",
            font=("Helvetica", 14),
            fg="green"
        )
        label3.pack(pady=10)

    show_sobriety_duration()

    window2.mainloop()
