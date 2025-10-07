from tkinter import *

root = Tk()

root.title("Login Form")
# root.iconbitmap('') # for favicon

root.minsize(400,400)

root.configure(bg='lightblue')

# Username label and entry
username_label = Label(root, text="Username:", bg='lightblue', font=('Arial', 12))
username_label.pack(pady=(40,5))
username_entry = Entry(root, font=('Arial', 12))
username_entry.pack(pady=5)

# Password label and entry
password_label = Label(root, text="Password:", bg='lightblue', font=('Arial', 12))
password_label.pack(pady=5)
password_entry = Entry(root, show='*', font=('Arial', 12))
password_entry.pack(pady=5)

# Login button
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "admin":
        result_label.config(text="Login Successful!", fg="green")
    else:
        result_label.config(text="Invalid credentials", fg="red")

login_button = Button(root, text="Login", command=login, font=('Arial', 12), bg='white')
login_button.pack(pady=10)

# Result label
result_label = Label(root, text="", bg='lightblue', font=('Arial', 12))
result_label.pack(pady=10)

root.mainloop()