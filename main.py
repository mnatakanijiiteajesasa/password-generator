from tkinter import *
from random import randint, shuffle, choice
from tkinter import messagebox

# Password Generator subprogram


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)

# Saving the info in a file and clearing the entries


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 and len(email) == 0 and len(password) == 0:
        messagebox.showinfo(title="Oops", message="You must fill all fields to proceed!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered:\n Website: {website} "
                                                              f"\nEmail: {email}\n Password: {password}"
                                                              f"\nDo you want to save?")
        if is_ok:
            with open("data.txt", "a") as datafile:
                datafile.write(f"{website} | {email} | {password}")
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


# User Interface

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=100, pady=100)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email")
email_label.grid(row=2, column=0)

email_input = Entry(width=25)
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="ADD", command=save)
add_button.grid(row=4, column=1, columnspan=3)


window.mainloop()
