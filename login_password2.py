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
        us_name = input("Enter your name: ").strip().capitalize()
        while not us_name.isalpha() or self.is_empty(us_name):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
            -> input doesn't consists of only letters
            -> input an empty""")
            us_name = input("Enter your name: ").strip().capitalize()

        us_age = input("Enter your age: ").strip()
        while not us_age.isnumeric() or self.is_empty(us_age):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                        -> input doesn't consists of only numbers
                        -> input an empty""")
            us_age = input("Enter your age: ").strip()

        us_login = input("Enter your login [nickname]: ").strip().lower()
        while not us_login.isalnum() or self.is_empty(us_login):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                        -> input doesn't consists of only letters and numbers
                        -> input an empty""")
            us_login = input("Enter your login [nickname]: ").strip().lower()

        us_password = input("Enter your password: ").strip()
        while not us_password.isalnum() or self.is_empty(us_password):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                        -> input doesn't consists of only letters and numbers
                        -> input an empty""")
            us_password = input("Enter your password: ").strip()

        self.name = us_name
        self.age = us_age
        self.login = us_login
        self.password = us_password
        self.save_to_database()



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

    @staticmethod
    def is_empty(str_):
        return not bool(str_)

    def save_to_database(self):
        mycursor.execute(f"insert into login_pasword(name, age, login, password) values ('{self.name}', {self.age}, '{self.login}', '{self.password}')")
        my_db.commit()


person = Project()
person.enterance()