from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()

window.title("Institute Login")
window.geometry("400x300")

# Heading
Label(window, text="Institute Login", font=("Arial", 16, "bold")).pack(pady=20)

# Email
Label(window, text="Email").pack()
entry_email = Entry(window, width=30)
entry_email.pack()

# Password
Label(window, text="Password").pack()
entry_password = Entry(window, width=30, show="*")
entry_password.pack()

# Login Button
Button(window, text="Login", width=20).pack(pady=20)

window.mainloop()