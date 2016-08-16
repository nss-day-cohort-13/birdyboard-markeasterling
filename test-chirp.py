import unittest
from birdyboard import *
from user import *
from chirp import *


class TestChirp(unittest.TestCase):

    def test_private_chirp_creation(self):
        self.author = User("mike", "mikeyboy")
        self.recipient = User("larry", "scary larry")
        self.message = "Hello Larry"
        self.chirp = PrivateChirp(self.message,
                                  self.author.unique_user_ID,
                                  self.recipient.unique_user_ID)

        self.assertEqual(self.message, self.chirp.message)
        self.assertEqual(self.chirp.author, self.author.unique_user_ID)
        self.assertEqual(self.chirp.recipient, self.recipient.unique_user_ID)
        self.assertIsNotNone(self.chirp.chirp_ID)
        self.assertIsInstance(self.chirp, PrivateChirp)
        # self.assertIsNotNone(chirp.chirp_time)

    def test_public_chirp_creation(self):
        self.author = User("mike", "mikeyboy")
        # self.recipient = User("larry", "scary larry")
        self.message = "Hello Larry"
        self.chirp = PublicChirp(self.message, self.author.unique_user_ID)


        self.assertEqual(self.message, self.chirp.message)
        self.assertEqual(self.chirp.author, self.author.unique_user_ID)
        self.assertIsNotNone(self.chirp.chirp_ID)
        self.assertIsInstance(self.chirp, PublicChirp)
        # self.assertIsNotNone(chirp.chirp_time)

if __name__ == '__main__':
    unittest.main()
