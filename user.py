import pickle
import uuid

class User:

        def __init__(self, fullname, screenname):
            self.screen_name = screenname
            self.full_name = fullname
            self.unique_user_ID = str(uuid.uuid1())
            print(self.unique_user_ID)
            # self.serialize_user()


if __name__ == '__main__':
    user1 = User("dave", "davesauce")
    # print(user1.deserialize_user())


