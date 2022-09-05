# to add: database
# email feature
# password attempts
# Change password


from fileinput import close
from tkinter import *
from tkinter import messagebox
from tkinter import Entry
from tkinter import Label
import time

storage = {'smith': 'sdf', 'johnson': 'sdfsdf',
           'terry': 'sdfsdfsdf', 'wowzers': 'sdf@sdf@sdf'}
user_requirements = '''Usernames must be: \n\t 1. 5 characters or longer \n\t 2. Completely Unique'''
pass_requirements = '''Passwords must: \n\t 1. be greater than 7 characters \n\t 2. contain numbers \n\t 3. not contain username \n\t 4. match  '''


def register():

    stockview = Tk()
    stockview.geometry("400x200+300+300")
    Label1 = Label(stockview, text="Create a username: ")

    Label1.place(x=5, y=30)
    global Entere1, Entere2, Entere3
    Entere1 = Entry(stockview, bd=5)
    Entere1.place(x=120, y=30)

    Label2 = Label(stockview, text="Create a password: ")
    Label2.place(x=5, y=70)
    Entere2 = Entry(stockview, bd=5)
    Entere2.place(x=120, y=70)

    Label2 = Label(stockview, text="Confirm password: ")
    Label2.place(x=5, y=110)
    Entere3 = Entry(stockview, bd=5)
    Entere3.place(x=120, y=110)

    submitbut = Button(stockview, text="Submit",
                       bd="5", command=username_check)
    submitbut.place(x=80, y=140)


def username_check():
    reg_username = Entere1.get().lower()
    reg_password = Entere2.get().strip()
    reg_confirmpass = Entere3.get().strip()
    checker = reg_username == reg_password
    while True:
        if reg_username in storage or len(reg_username) < 5:
            messagebox.showinfo("Check Username", user_requirements)
            break
        elif reg_password != reg_confirmpass or checker != False or len(reg_password) <= 7:
            messagebox.showinfo('Please Try Again,', pass_requirements)
            break
        else:
            messagebox.showinfo(
                "Completed", 'New Account Created, Try logging in')
            break

    storage.update({reg_username: reg_password})


def login():

    print('--login Page')
    username = Enter1.get()
    password = Enter2.get()

    p = 5
    while p != 0:
        try:
            if storage[username] == password:
                loginLabe = Label(stockview, text="Login Successful!")
                loginLabe.pack(side='bottom')
                time.sleep(3)
                stockview.destroy()
                break
            elif storage[password] == username:
                loginLabe
                loginLabe.pack(side='right')
                time.sleep(3)
                stockview.destroy()
                break

        except:
            st = messagebox.askquestion(
                "Invalid Entry", "Would you like to register for an account?:", icon="question")
            if st == "yes":
                register()
                break
            elif st == "no":
                break

            # else:
            #    fss2 = "Warning, {} attempt left\n\t"
            #    messagebox.showinfo("Warning", fss2.format(p))
                #  Label(stockview, text = ("Locked Out"))
            #    stockview.destroy()


stockview = Tk()
stockview.title("Stockview")
stockview.resizable(False, False)
stockview.geometry("225x200")

Labe1 = Label(stockview, text="Username")
Labe1.place(x=5, y=30)
Enter1 = Entry(stockview, bd=5)
Enter1.place(x=65, y=30)


Labe2 = Label(stockview, text="Password").place(x=5, y=70)
Enter2 = Entry(stockview, bd=5, show="*")
Enter2.place(x=65, y=70)

but = Button(stockview, text="Login", bd="5", command=login)
but.place(x=90, y=110)
Regbut = Button(stockview, text="Regsiter", bd="10", command=register)
Regbut.place(x=80, y=140)


stockview.mainloop()
