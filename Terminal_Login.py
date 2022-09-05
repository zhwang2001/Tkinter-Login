# TODO
# https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
# https://stackoverflow.com/questions/20061307/python-3-login-program-using-dictionaries
from time import time

storage = {'smith': 'sdf', 'johnson': 'sdfsdf', 'terry': 'sdfsdfsdf'}
user_requirements = '''Usernames must be: \n\t 1. 5 characters or longer \n\t 2. Completely Unique'''
pass_requirements = '''Passwords must: \n\t 1. be greater than 7 characters \n\t 2. contain numbers \n\t 3. not contain username \n\t 4. match  '''

print("--Create your new account\n\t")


def register():
    def username_check():

        reg_username = input("Create a username here: ").lower()
        while True:
            if reg_username in storage or len(reg_username) < 5:
                print(user_requirements)
                reg_username = input("Create a username here: ").lower()

            else:
                print("--Username Available")
                break

        def password_check():

            reg_password = input("Create a password here: ").strip()
            reg_confirmpass = input("Confirm password here: ").strip()

            checker = reg_username == reg_password
            while True:
                if reg_password == reg_confirmpass and checker == False and len(reg_password) > 7:
                    print('--Success!')
                    break

                elif reg_password != reg_confirmpass or checker != False or len(reg_password) <= 7:
                    checker = reg_username == reg_password
                    print('--Please Try Again,', pass_requirements)
                    reg_password = input("Create a password here: ").strip()
                    reg_confirmpass = input("Confirm password here: ").strip()
                    continue

                else:
                    break

            storage.update({reg_username: reg_password})

        password_check()

    username_check()


register()


def login():

    print('--login Page')
    username = input("Enter username here: ").lower()
    password = input("Enter password here: ").strip()

    while True:
        p = 5
        try:
            if storage[username] == password:
                print("--login successful")
                break
            elif storage[password] == username:
                print("--login successful")
                break

        except:
            st = input(
                "Would you like to register for an account? (y/n): ").strip().lower()
            if st == "y":
                register()
                login()
            elif st == "n":
                pass
            else:
                print("Invalid Repsonse")
                continue

            while p != 1:
                print("--Wrong username or password")
                p = p - 1
                if p != 1:
                    print("--", p, "attempts left\n\t")
                else:
                    print(p, " attempt left")
                username = input("Enter username here: ").lower()
                password = input("Enter password here: ").strip()
            print("Locked out")
            break


login()
