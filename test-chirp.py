import unittest
from birdyboard import *


class TestChirp(unittest.TestCase):

    def test_private_chirp_creation(self):
        self.author = User("mike", "mikeyboy")
        self.recipient = User("larry", "scary larry")
        self.chirp = Chirp(message="hello larry",
                      author=author.user_ID,
                      recipient=recipient.user_ID,
                      private=True
                          )

        self.assertEqual("hello larry", chirp.message)
        self.assertEqual(author, author.user_ID)
        self.assertEqual(recipient, recipient.user_ID)
        self.assertIsNotNone(chirp.chirp_ID)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_time)

    def test_public_chirp_creation(self):
        author = User("mike", "mikeyboy")
        recipient = User("larry", "scary larry")
        chirp = Chirp(message="hello larry",
                      author=author.user_ID,
                      private=False
                      )
        self.assertEqual("hello larry", chirp.message)
        self.assertEqual(author, author.user_ID)
        self.assertIsNotNone(chirp.chirp_ID)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_time)

if __name__ == '__main__':
    unittest.main()
