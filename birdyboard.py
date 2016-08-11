import pickle
import uuid

from user import *
# from chirp import *


class Birdyboard:

    def __init__(self):
        self.user_list = None
        self.chirp_list = []
        self.conversation_list = []
        self.current_user = None # should save as dict object so you can get any of the identifiers from it
        print(self.user_list)

    def main_menu(self):
        print("welcome to birdyboard!")
        print("1. new user")
        print("2. select user")
        self.selection = input("choose the number of your selection, then press enter > ")

        if self.selection == "1":
            self.create_new_user()

        if self.selection == "2":
            self.show_existing_users()

    def show_existing_users(self):
        self.user_list = User.deserialize_user(self)
        print("select chirper: ")
        counter = 1
        for item in self.user_list:
            print(str(counter) + ". " + item['screen name'])
            counter += 1
        current_user = input("type the number of your chosen chirper: ")
        Birdyboard.current_user = self.user_list[int(current_user) - 1]
        print("BIRDYBOARD CURRENT USER",Birdyboard.current_user)
        self.main_menu()

    def create_new_user(self):
        print("you are making a new user account:")
        self.fullname = input("enter your full name:")
        self.screenname = input("enter your desired screen name:")
        new_user = User(self.fullname, self.screenname)
        Birdyboard.current_user = new_user.user_object
        print("BIRDYBOARD CURRENT USER",Birdyboard.current_user)

        # print(new_user.screen_name)

        # self.user_list = new_user.deserialize_user()
        # print(self.user_list)
        self.main_menu()

if __name__ == '__main__':
    birdyboard = Birdyboard()
    birdyboard.main_menu()
#     birdyboard.user = birdyboard.User("dave", "davesauce")
