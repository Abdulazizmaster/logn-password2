import mysql.connector
import os

my_db = mysql.connector.connect(
    host='localhost',
    user='Abdulaziz',
    password='123123123',
    database='login_password2'
)
mycursor = my_db.cursor()
# mycursor.execute("select password from login_pasword where login='dado12'")
# all = mycursor.fetchall()
# print(all)


class Project:
    def __init__(self):
        self.name = None
        self.age = None
        self.login = None
        self.password = None

    def enterance(self):
        self.clear_everything()
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
            self.log_in()

    def register(self):
        self.clear_everything()
        print("\t\tRegister part\n")
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
        while not us_login.isalnum() or self.is_empty(us_login) or self.is_exists_in_database(us_login):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                    -> input doesn't consists of only letters and numbers
                    -> input an empty
                    -> this login is already taken""")
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
        self.enterance()

    def log_in(self):
        self.clear_everything()
        login = input("Input your login: ").strip().lower()
        while not login.isalnum() or self.is_empty(login) or not self.is_exists_in_database(login):
            self.clear_everything()
            print("""Invalid input. Possible errors:
                    -> input doesn't consists of only letters and numbers
                    -> input an empty""")
            print("Maybe you haven't registered yet. Do you wanna register? ")
            y_or_n = input(">>> ").strip().lower()
            options2 = ['y', 'n', 'yes', 'no']
            while y_or_n not in options2:
                self.clear_everything()
                print("Invalid input. Try again [y/n]: ")
                y_or_n = input(">>> ").strip().lower()
            if y_or_n == options2[0] or y_or_n == options2[2]:
                self.register()
            else:
                self.log_in()
                break

        password = input("Input your password: ").strip()
        while not password.isalnum() or self.is_empty(password) or self.is_correct_password(login,password):
            self.clear_everything()
            print("""Invalid input. Possible errors:
                    -> input doesn't consists of only letters and numbers
                    -> input an empty
                    -> uncorrect password""")
            password = input("Input your password: ").strip()

        self.login = login
        self.password = password

        self.clear_everything()
        self.second_msg()
        options3 = ['1','2','3']
        new_msg = input(">>> ").strip()
        while new_msg not in options3:
            self.clear_everything()
            print("Invalid input. You can only enter [1,2]")
            new_msg = input(">>> ").strip()
        if new_msg == options3[0]:
            self.update_login_password()
        elif new_msg == options3[1]:
            self.log_out()
        else:
            self.delete_profile()

    def update_login_password(self):
        new_login = input("Input your new login: ").strip().lower()
        while not new_login.isalnum() or self.is_empty(new_login) or self.is_exists_in_database(new_login):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                    -> input doesn't consists of only letters and numbers
                    -> input an emptyself.login
                    -> this login is already taken""")
            new_login = input("Input your new login: ").strip().lower()

        new_password = input("Input your new password: ").strip()
        while not new_password.isalnum() or self.is_empty(new_password):
            self.clear_everything()
            print("""Invalid input. Possible errors: 
                    -> input doesn't consists of only letters and numbers
                    -> input an empty""")
            new_password = input("Input your new password: ").strip()

        self.update_in_database(new_login,new_password)
        print("Your login and password successfully updated!")

    def log_out(self):
        self.enterance()

    def delete_profile(self):
        mycursor.execute(f"delete from login_pasword where login='{self.login}'")
        my_db.commit()
        print("Your profile has been deleted!")

    @staticmethod
    def first_msg():
        print("""
             Welcome!
        
        What do you want to do:
        [1] -> Register
        [2] -> Log in""")

    @staticmethod
    def second_msg():
        print("""You've successfully logged in!
        
          Menu: -> [1] Update login and password
                -> [2] Log out
                -> [3] Delete profile""")

    @staticmethod
    def clear_everything():
        os.system("clear")

    @staticmethod
    def is_empty(str_):
        return not bool(str_)

    def save_to_database(self):
        mycursor.execute(f"insert into login_pasword(name, age, login, password) values ('{self.name}', {self.age}, '{self.login}', '{self.password}')")
        my_db.commit()

    @staticmethod
    def is_exists_in_database(login):
        mycursor.execute("select login from login_pasword")
        logins = mycursor.fetchall()
        for i in logins:
            if login == i[0]:
                return True
        return False

    @staticmethod
    def is_correct_password(login,password):
        mycursor.execute("select login from login_pasword")
        logins = mycursor.fetchall()
        mycursor.execute("select password from login_pasword")
        passwords = mycursor.fetchall()
        log = ""
        passw = ""
        for i in logins:
            if login == i[0]:
                log = i[0]
        for i in passwords:
            if password == i[0]:
               passw = i[0]

        mycursor.execute(f"select password from login_pasword where login='{log}'")
        passw2 = mycursor.fetchall()
        if passw == passw2[0][0]:
            return False
        return True

    def update_in_database(self,login,password):
        mycursor.execute(f"update login_pasword set login='{login}', password='{password}' where login='{self.login}'")
        my_db.commit()


person = Project()
person.enterance()

