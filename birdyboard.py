import pickle
import uuid

from user import *
# from chirp import *
from chirp import *


class Birdyboard:

    def __init__(self):
        self.user_list = None
        self.chirp_list = []
        self.conversation_list = []
        self.current_user = None # should save as dict object so you can get any of the identifiers from it
        print(self.user_list)

    def main_menu(self):
        print("welcome to birdyboard!")
        print("1. New User")
        print("2. Select User")
        print("3. View Public Chirps")
        print("4. View Private Chirps")
        print("5. New Public Chirp")
        print("6. New Private Chirp")
        print("7. Exit Program")


        self.selection = input("choose the number of your selection, then press enter > ")

        if self.selection == "1":
            self.create_new_user()

        if self.selection == "2":
            self.show_existing_users()

        if self.selection == "3":
            self.view_public_chirps()

        if self.selection == "4":
            self.view_private_chirps()

        if self.selection == "5":
            self.new_public_chirp()

        if self.selection == "6":
            self.new_private_chirp()


    def show_existing_users(self):
        self.user_list = User.deserialize_user(self)
        print("select chirper: ")
        counter = 1
        for item in self.user_list:
            print(str(counter) + ". " + item['screen name'])
            counter += 1
        current_user = input("type the number of your chosen chirper: ")
        Birdyboard.current_user = self.user_list[int(current_user) - 1]
        print("BIRDYBOARD CURRENT USER", Birdyboard.current_user)
        print("You are now signed in as: " + Birdyboard.current_user["screen name"])
        self.main_menu()

    def create_new_user(self):
        print("you are making a new user account:")
        self.fullname = input("enter your full name:")
        self.screenname = input("enter your desired screen name:")
        new_user = User(self.fullname, self.screenname)
        Birdyboard.current_user = new_user.user_object
        print("BIRDYBOARD CURRENT USER", Birdyboard.current_user)
        print("You are now signed in as: " + Birdyboard.current_user["screen name"])

        # print(new_user.screen_name)
        # self.user_list = new_user.deserialize_user()
        # print(self.user_list)
        self.main_menu()

    def new_public_chirp(self):
        print("What do you want to chirp?")
        self.message = input("> ")
        new_chirp = PublicChirp(self.message, Birdyboard.current_user["uuid"])
        print("chirp created!")
        print("")
        self.main_menu()

    def view_public_chirps(self):
        self.public_chirp_list = PublicChirp.deserialize_chirp(self)
        self.user_list = User.deserialize_user(self)
        # print(self.public_chirp_list)
        print("type a number to view the conversation")
        counter = 1
        for chirp in self.public_chirp_list:
            for user in self.user_list:
                if user["uuid"] == chirp["author"]:
                    print(str(counter)  + ". " + user["screen name"] + ": " + chirp['message'])
                    counter += 1





        # self.main_menu()




if __name__ == '__main__':
    birdyboard = Birdyboard()
    birdyboard.main_menu()
#     birdyboard.user = birdyboard.User("dave", "davesauce")
