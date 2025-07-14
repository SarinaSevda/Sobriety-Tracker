
# styles.py

import tkinter as tk
from tkinter import ttk

def configure_styles():
    style = ttk.Style()




WELCOME_LABEL_STYLE = {
    "font": ("Helvetica", 20, "bold"),
    "wraplength": 500,
    "justify": "center",
}


NAME_LABEL_STYLE = {
    "font": ("Helvetica", 20, "bold"),
    "wraplength": 500,
    "justify": "center",
}


ADDICTION_LABEL_STYLE = {
    "font": ("Helvetica", 13),
    "wraplength": 500,
    "justify": "center",
}


GOAL_LABEL_STYLE = {
    "font": ("Helvetica", 13),
    "wraplength": 500,
    "justify": "center",
}

def set_dropdown_font(dropdown, font=("Helvetica", 13)):
    dropdown["menu"].config(font=font)


SOBRIETY_LABEL_STYLE = {
    "font": ("Helvetica", 13),
    "wraplength": 500,
    "justify": "center",
}


FINAL_LABEL_STYLE = {
    "font": ("Helvetica", 14),
    "wraplength": 500,
    "justify": "center",
}


QUOTE_LABEL_STYLE = {
    "font": ("Helvetica", 13, "italic"),
    "foreground": "SkyBlue1",
    "background": "white",
    "wraplength": 500,
    "justify": "center",
}

#Timer-GUI

TIMER_OVAL_STYLE = {
    "outline": "grey",
    "width": 3
}

TIMER_RECT_STYLE = {
    "outline": "lavender",
    "width": 2,
    "fill": "white"
}

TIMER_TEXT_STYLE = {
    "font": ("Helvetica", 14, "bold")
}


DATENTIME_LABEL_STYLE = {
    "font": ("Helvetica", 10),
    "fill": "gray"
}


CHALLENGE_LABEL_UNLOCKED = {
    "font": ("Helvetica", 12, "bold"),
    "foreground": "green",
}

CHALLENGE_LABEL_LOCKED = {
    "font": ("Helvetica", 12),
    "foreground": "grey",
}

CHALLENGE_LABEL_DEFAULT = {
    "font": ("Helvetica", 18),
}

SETTINGS_LABEL_STYLE = {
    "font": ("Helvetica", 16, "bold"),
    "wraplength": 500,
    "justify": "center",
}

REFLECTION_LABEL_STYLE = {
    "font": ("Helvetica", 14, "bold"),
    "wraplength": 500,
    "justify": "center"
}

TEXT_ENTRY_STYLE = {
    "font": ("Helvetica", 12)
}

NOTE_TEXT_STYLE = {
    "bg": "white",
    "fg": "black",
    "font": ("Helvetica", 11),
    "relief": "sunken",
    "bd": 1
}


def help_label(master, text, style, pady=2):
    label = tk.Label(master, text=text, **style)
    label.pack(anchor='w', pady=pady, fill='x')
    return label

HELP_LABEL_STYLE = {
    "normal": {
        "font": ("Helvetica", 12),
        "wraplength": 500,
        "justify": "left",
        "anchor": "w",
    },
    "bold": {
        "font": ("Helvetica", 12, "bold"),
        "wraplength": 500,
        "justify": "left",
        "anchor": "w",
    },
}

def apply_theme(style: ttk.Style, dark_mode: bool, window=None):
    """
    Wendet entweder den Dark Mode oder das helle Standard-Theme an.
    """
    if dark_mode:
        style.configure(".", background="#2e2e2e", foreground="white")
        style.configure("TLabel", background="#2e2e2e", foreground="white")
        style.configure("TButton", background="#444444", foreground="black")
        style.configure("TCheckbutton", background="#2e2e2e", foreground="white")
        style.configure("TEntry", fieldbackground="#444444", foreground="white")
    else:
        style.configure(".", background="white", foreground="black")
        style.configure("TLabel", background="white", foreground="black")
        style.configure("TButton", background="white", foreground="black")
        style.configure("TCheckbutton", background="white", foreground="black")
        style.configure("TEntry", fieldbackground="white", foreground="black")

    if window:
        window.configure(bg=style.lookup(".", "background"))
