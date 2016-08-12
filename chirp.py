import pickle
import uuid


class PrivateChirp:

    def __init__(self, text, creator, reciever):
        self.author = creator
        self.recipient = reciever
        self.message = text
        self.chirp_ID = uuid.uuid4().int
        self.private_chirp_object = {"chirp_id": self.chirp_ID ,"author": self.author, "recipient": self.recipient, "message": self.message}
        print("PRIVATE CHIRP OBJ ",self.private_chirp_object)
        self.serialize_chirp()

    def serialize_chirp(self):

        with open('privatechirp.txt', "ab+") as f:
            pickle.dump(self.private_chirp_object, f)


    def deserialize_chirp(self):

        self.private_chirps = []
        with open('privatechirp.txt', "rb") as f:
            while True:
                try:
                    self.private_chirps.append(pickle.load(f))
                except EOFError:
                    break
        return self.private_chirps

class PublicChirp:

    def __init__(self, text, creator):
        self.author = creator
        self.message = text
        self.chirp_ID = uuid.uuid4().int
        self.public_chirp_object = {"chirp_id": self.chirp_ID, "author": self.author, "message": self.message}
        print("PUBLIC CHIRP OBJ ", self.public_chirp_object)
        self.serialize_chirp()

    def serialize_chirp(self):

        with open('publicchirp.txt', "ab+") as f:
            pickle.dump(self.public_chirp_object, f)


    def deserialize_chirp(self):

        self.public_chirps = []
        with open('publicchirp.txt', "rb") as f:
            while True:
                try:
                    self.public_chirps.append(pickle.load(f))
                except EOFError:
                    break
        return self.public_chirps
