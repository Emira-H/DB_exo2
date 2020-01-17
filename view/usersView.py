from model.usersModel import UsersModel

class UsersView:
    def __init__(self):
        self.um = UsersModel()

    def to_create_an_account(self):
        name = input("enter your name:")
        firstname = input("enter your firstname:")
        pseudo = input("enter your pseudo:")
        mail = input("enter your mail:")
        age = int(input("enter your age:"))
        password = input("enter your password:")
        self.um.create_an_account(name, firstname, pseudo, mail, age, password)

    def to_connect_existing_account(self):
        pseudo = input("enter your pseudo: ")
        password = input("enter your password: ")
        self.um.connect_existing_account(pseudo, password)
