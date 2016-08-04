import unittest
from birdyboard import *


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        self.user = User("bob vila", "bob_the_builder")

        self.assertEqual("bob vila", user.full_name)
        self.assertEqual("bob_the_builder", user.screen_name)
        self.assertIsNotNone(user.user_ID)
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
