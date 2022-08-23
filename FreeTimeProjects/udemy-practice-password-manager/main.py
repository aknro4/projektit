import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

DEFAULT_EMAIL = "aarokolu.ak@gmail.com"
window = Tk()

# ---------------------------- FIND PASSWORD ------------------------------- #


def search():

    label_row = 1
    entry_row = 2

    new_window = Toplevel(window)
    new_window.title("Saved passwords")
    new_window.config(padx=50, pady=50, )

    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        Label(new_window, text="No data found.").pack()

    for i in data:
        # Website label
        label_email = Label(new_window, text=f"Website: {i}")
        label_email.grid(column=0, row=label_row)
        label_row += 1
        # Email label
        label_email = Label(new_window, text="Email:")
        label_email.grid(column=0, row=label_row)
        label_row += 1
        # Password label
        label_email = Label(new_window, text="Password:")
        label_email.grid(column=0, row=label_row)
        label_row += 1

        # Email entry
        entry_email = Entry(new_window, width=35)
        entry_email.insert(0, data[i]['email'])
        entry_email.grid(column=1, row=entry_row)
        entry_row += 1
        # Password entry
        entry_password = Entry(new_window, width=35)
        entry_password.insert(0, data[i]['password'])
        entry_password.grid(column=1, row=entry_row)
        entry_row += 2

    # website = website_input.get()
    #
    # try:
    #     with open("data.json") as file:
    #         data = json.load(file)
    # except FileNotFoundError:
    #     messagebox.showinfo(title="Error", message="File was not found")
    # else:
    #     # Could have done this whit if else statement
    #     try:
    #         messagebox.showinfo(title="Password", message=f"Website: {website}\n"
    #                                                       f"Email: {data[website]['email']}\n"
    #                                                       f"Password: {data[website]['password']}")
    #     except KeyError:
    #         messagebox.showinfo(title="Error", message="Website not found, try again")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field", message="Don't leave fields empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window.title("Password Manager")
window.config(padx=50, pady=50, )

# LOGO
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website")
website_label.grid(column=0, row=1, sticky="EW")

# Email label
email_username_label = Label(text="Email/Username")
email_username_label.grid(column=0, row=2, sticky="EW")

# Password label
password_label = Label(text="Password")
password_label.grid(column=0, row=3, sticky="EW")

# Website entry
website_input = Entry(width=20)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

# Email entry
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_input.insert(0, DEFAULT_EMAIL)

# Password entry
password_input = Entry(width=20)
password_input.grid(column=1, row=3, sticky="EW")

# Generate password button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW", )

# Add button to add info to file
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", )

# Search button
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")

mainloop()
