from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.askretrycancel(title="Missing Info", message=f"You are missing the website or password details")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"You entered the following details:\nwebsite:{website}\nusername:{username}\npassword:{password}\nIs this okay?")
        if is_ok:
            new_data = {
                website: {
                    "username": username,
                    "password": password
                }
            }
            try:
                with open("data.json", "r") as data_file:
                    content = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                content.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(content, data_file, indent=4)
            finally:
                messagebox.showinfo(title="Successful", message="Your details have been saved")
                website_entry.delete(0, END)
                website_entry.focus()
                password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Data Not Found",
                            message="Oops!!!\nLooks like you don't have any data with us right now. Enter the details and press add to manage passwords.")
    else:
        try:
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title="Data Not Found", message=f"The data for {website} is not stored with us")
        else:
            messagebox.showinfo(title=website, message=f"website: {website}\npassword: {password}")


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(window, height=400, width=400)

img = canvas.create_image(200, 200, image=lock_img)

website_label = Label(text="Website ")
username_label = Label(text="Email/Username ")
password_label = Label(text="Password ")

website_entry = Entry(width=39)
website_entry.focus()
username_entry = Entry(width=65)
username_entry.insert(0, "yogesh@gmail.com")
password_entry = Entry(width=39)

generate_password_button = Button(text="Generate Password", width=21, command=generate)
add_button = Button(text="Add", command=save, width=60)
search_button = Button(text="Search", width=21, command=search)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry.grid(row=1, column=1)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

window.mainloop()
