import pickle
import uuid


class User:

        def __init__(self, fullname, screenname):
            self.screen_name = screenname
            self.full_name = fullname
            self.unique_user_ID = str(uuid.uuid1())
            self.user_object = {"uuid": self.unique_user_ID, "full name": self.full_name, "screen name": self.screen_name}
            print(self.unique_user_ID)
            self.serialize_user()

        def serialize_user(self):
            try:
                self.user_dict.update({"uuid": self.unique_user_ID, "full name": self.full_name, "screen name": self.screen_name})
                with open('users.txt', "ab+") as f:
                    pickle.dump(self.user_dict, f)
                    print("try")
            except:
                self.user_dict = {}
                self.user_dict.update({"uuid": self.unique_user_ID, "full name": self.full_name, "screen name": self.screen_name})
                with open('users.txt', "ab+") as f:
                    pickle.dump(self.user_dict, f)
                    print("except")

        def deserialize_user(self):
            self.users = []
            with open('users.txt', "rb") as f:
                while True:
                    try:
                        self.users.append(pickle.load(f))
                    except EOFError:
                        break
            return self.users



if __name__ == '__main__':
    user1 = User("dave", "davesauce")
    # print(user1.deserialize_user())


