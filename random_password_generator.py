from tkinter import *
import random
import string

# Initialize the main window
root = Tk()
root.geometry("400x200")  # Set window size

# Variables to hold password and its length
passstr = StringVar()
pwd_len = IntVar()

# Function to generate the password
def get_pass():
    # Combine ASCII letters, digits, and punctuation for password characters
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""
    # Generate password of specified length
    for x in range(pwd_len.get()):
        password += random.choice(pass1)
    passstr.set(password)  # Update the password variable

# GUI setup
Label(root, text="Password Generator", font="calibri 18 bold").pack()
Label(root, text="Enter length of Password").pack(pady=9)
Entry(root, textvariable=pwd_len).pack(pady=2)  # For inputting password length
Button(root, text="Generate Password", command=get_pass).pack(pady=15)  # Triggers password generation
Entry(root, textvariable=passstr).pack(pady=2)  # Displays generated password

# Run the GUI application
root.mainloop()
