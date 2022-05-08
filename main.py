from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:
        messagebox.showwarning(title='Invalid Input', message='Please fill all fields correctly')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'You have entered the following\n'
                                                              f'Email/Username: {username}\nPassword: {password}\n'
                                                              f'Is it correct?')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{website} | {username} | {password}\n')
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1, sticky='WE')
username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2, sticky='WE')
password_label = Label(text='Password:')
password_label.grid(column=0, row=3, sticky='WE')
# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky='EW')
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
username_entry.insert(0, 'yourEmail@email.com')
password_entry = Entry(width=21, show='*')
password_entry.grid(column=1, row=3, sticky='EW')
# Buttons
password_gen_btn = Button(text='Generate Password', command=generate_password)
password_gen_btn.grid(column=2, row=3, sticky='EW')
add_btn = Button(text='Add', width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky='EW')
window.mainloop()
