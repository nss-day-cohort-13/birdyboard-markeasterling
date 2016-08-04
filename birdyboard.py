import uuid


class Birdyboard:

    def __init__(self):
        self.user_list = []
        self.chirp_list = []
        self.conversation_list = []
        self.current_user = None

    class User:

        def __init__(self, fullname, screenname):
            self.screen_name = screenname
            self.full_name = fullname
            self.unique_user_ID = str(uuid.uuid1())
            print(self.unique_user_ID)


# if __name__ == '__main__':
#     birdyboard = BirdyBoard()
#     birdyboard.user = birdyboard.User("dave", "davesauce")
