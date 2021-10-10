import mysql.connector
import os

my_db = mysql.connector.connect(
    host='localhost',
    user='Abdulaziz',
    password='123123123',
    database='login_password2'
)

mycursor = my_db.cursor()


class Project:
    def __init__(self):
        self.name = None
        self.age = None
        self.login = None
        self.password = None

    def enterance(self):
        self.first_msg()
        enter_ = input(">>> ").strip()
        options = ['1','2']
        while enter_ not in options:
            self.clear_everything()
            print("Invalid input. You can only enter [1,2,3,4]")
            enter_ = input(">>> ").strip()

        if enter_ == options[0]:
            self.register()
        else:
            self.login()

    def register(self):
        pass

    def log_in(self):
        pass

    def update_login_password(self):
        pass

    def log_out(self):
        pass

    def delete_profile(self):
        pass

    @staticmethod
    def first_msg():
        print("""
             Welcome!
        
        What do you want to do:
        [1] -> Register
        [2] -> Log in""")

    @staticmethod
    def clear_everything():
        os.system("clear")


person = Project()
person.enterance()