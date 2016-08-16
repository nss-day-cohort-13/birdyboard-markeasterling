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
        # self.current_recipient = None
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
        self.current_user = self.user_list[int(current_user) - 1]
        print("BIRDYBOARD CURRENT USER", self.current_user)
        print("You are now signed in as: " + self.current_user["screen name"])
        self.main_menu()

    def create_new_user(self):
        print("you are making a new user account:")
        self.fullname = input("enter your full name:")
        self.screenname = input("enter your desired screen name:")
        new_user = User(self.fullname, self.screenname)
        self.current_user = new_user.user_object
        print("BIRDYBOARD CURRENT USER", self.current_user)
        print("You are now signed in as: " + self.current_user["screen name"])

        # print(new_user.screen_name)
        # self.user_list = new_user.deserialize_user()
        # print(self.user_list)
        self.main_menu()

    def new_public_chirp(self):
        print("What do you want to chirp? (public chirp")
        self.message = input("> ")
        new_chirp = PublicChirp(self.message, Birdyboard.current_user["uuid"])
        print("chirp created!")
        print("")
        self.main_menu()

    def new_private_chirp(self):
        print("Who do you want to send a chirp?")

        self.user_list = User.deserialize_user(self)
        print("select chirper: ")
        counter = 1
        for item in self.user_list:
            print(str(counter) + ". " + item['screen name'])
            counter += 1
        recipient_position = input("type the number who you'd like to chirp: ")
        self.recipient = self.user_list[int(recipient_position) - 1]["uuid"]

        print("What do you want to chirp? (private chirp)")
        self.message = input("> ")
        new_chirp = PrivateChirp(self.message, Birdyboard.current_user["uuid"], self.recipient, convoID = None)
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


    def view_private_chirps(self):
        self.private_chirp_list = PrivateChirp.deserialize_chirp(self)
        self.user_list = User.deserialize_user(self)
        self.users_chirps = []
        print("THIS IS THE CURRENT USER",self.current_user)
        # print(self.public_chirp_list)
        print("type a number to view the conversation")
        counter = 1
        for chirp in self.private_chirp_list:
            if chirp["recipient"] == self.current_user["uuid"]:
                self.users_chirps.append(chirp)

                for chirp in self.users_chirps:
                    for user in self.user_list:
                        if user["uuid"] == chirp["author"]:
                            print(str(counter) + ". " + user["screen name"] + ": " + chirp['message'])
                            counter += 1

        self.chosen_chirp = int(input("> "))
        self.chirp_conversation_starter = self.users_chirps[self.chosen_chirp - 1]["convo_ID"]
        print("THIS WAS THE CHOSEN CHIRP",self.users_chirps[self.chosen_chirp - 1])

        # convo_counter = 1
        # for chirps in private_chirp_list:
        #     if chirp["convo_ID"] == self.chirp_conversation_starter:
        #         for user in self.user_list:
        #             if user["uuid"] == chirp["author"]:
        #                     print(str(counter) + ". " + user["screen name"] + ": " + chirp['message'])
        #                     convo_counter += 1

        print("1. Reply")
        print("2. Back")
        self.reply_action = input("> ")
        if self.reply_action == "1":
            self.reply_to_private_chirp(self.chirp_conversation_starter, )

        if self.reply_action == "2":
            self.main_menu()

    def reply_to_private_chirp(self, convoID):
        self.convo_ID = convoID
        print("THIS IS THE CONVERSATION ID: ", self.convo_ID)
        self.private_chirp_list = PrivateChirp.deserialize_chirp(self)
        self.user_list = User.deserialize_user(self)
        for chirp in self.private_chirp_list:
            if chirp["convo_ID"] == self.convo_ID:
                self.recipient = chirp["recipient"]

        print("What do you want to add to this conversation?")
        self.reply = input("> ")
        self.new_reply = PrivateChirp(self.reply, self.current_user["uuid"], self.recipient, self.convo_ID)











        # self.main_menu()




if __name__ == '__main__':
    birdyboard = Birdyboard()
    birdyboard.main_menu()
#     birdyboard.user = birdyboard.User("dave", "davesauce")
