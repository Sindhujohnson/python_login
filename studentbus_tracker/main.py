from tkinter import *
from tkinter import messagebox
import sqlite3

# Function
def register():

    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm = entry_confirm.get()

    if name == "" or email == "" or password == "" or confirm == "":
        messagebox.showerror("Error", "Please fill all fields")

    elif password != confirm:
        messagebox.showerror("Error", "Passwords do not match")

    else:
        conn = sqlite3.connect("database/tracker.db")
        cursor = conn.cursor()
        cursor.execute("""
INSERT INTO institute(institute_name, email, password)
VALUES (?, ?, ?)
""", (name, email, password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Registration Successful")


# Window
window = Tk()
window.title("Institute Registration")
window.geometry("1000x800")

# Heading
Label(window, text="Institute Registration", font=("Arial", 20, "bold")).pack(pady=40)

# Name
Label(window, text="Institute Name").pack()
entry_name = Entry(window, width=30)
entry_name.pack()

# Email
Label(window, text="Email").pack()
entry_email = Entry(window, width=30)
entry_email.pack()

# Password
Label(window, text="Password").pack()
entry_password = Entry(window, width=30, show="*")
entry_password.pack()

# Confirm Password
Label(window, text="Confirm Password").pack()
entry_confirm = Entry(window, width=30, show="*")
entry_confirm.pack()

# Register Button
Button(window, text="Register", command=register).pack(pady=20)

window.mainloop()