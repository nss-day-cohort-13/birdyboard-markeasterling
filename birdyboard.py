import pickle
import uuid

from user import *
# from chirp import *


class Birdyboard:

    def __init__(self):
        self.user_list = None
        self.chirp_list = []
        self.conversation_list = []
        self.current_user = None
        print(self.user_list)

    def menu(self):
        print("welcome to birdyboard")
        print("1. new user")
        print("2. select user")
        self.selection = input("choose the number of your selection, then press enter > ")

        if self.selection == "1":
            print("you are making a new user account:")
            self.fullname = input("enter your full name:")
            self.screenname = input("enter your desired screen name:")
            new_user = User(self.fullname, self.screenname)

if __name__ == '__main__':
    birdyboard = Birdyboard()
    birdyboard.menu()
#     birdyboard.user = birdyboard.User("dave", "davesauce")
