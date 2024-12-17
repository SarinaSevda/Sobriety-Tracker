import tkinter as tk

root = tk.Tk()

root.title('Sobriety Tracker')
root.geometry('500x500')
root.configure(bg="white")
root.resizable(False, False)

label = tk.Label(root, text="Willkommen Emma!", font=("Helvetica", 14), bg="lightblue")
label.pack(pady=20)  # Pack-Layoutmanager mit Abstand (pady)

# Starte die Hauptschleife
root.mainloop()

