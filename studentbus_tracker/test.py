from tkinter import *
from tkinter import messagebox

# Create window
window = Tk()

window.title("Institute Registration")
window.geometry("500x450")

# Heading
heading = Label(window, text="Institute Registration", font=("Arial", 16, "bold"))
heading.pack(pady=20)

# Institute Name
Label(window, text="Institute Name").pack()
entry_name = Entry(window, width=30)
entry_name.pack(pady=5)

# Email
Label(window, text="Email").pack()
entry_email = Entry(window, width=30)
entry_email.pack(pady=5)

# Password
Label(window, text="Password").pack()
entry_password = Entry(window, width=30, show="*")
entry_password.pack(pady=5)

# Confirm Password
Label(window, text="Confirm Password").pack()
entry_confirm = Entry(window, width=30, show="*")
entry_confirm.pack(pady=5)

# Register Button
Button(window, text="Register", command="register").pack(pady=20)
# Enter the value.
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
        messagebox.showinfo("Success", "Registration Successful")

window.mainloop()