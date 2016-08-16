import unittest

from user import *

from birdyboard import *


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        self.user = User("bob vila", "bob_the_builder")
        self.assertEqual("bob vila", self.user.full_name)
        self.assertEqual("bob_the_builder", self.user.screen_name)
        self.assertIsNotNone(self.user.unique_user_ID)
        self.assertIsInstance(self.user, User)


if __name__ == '__main__':
    unittest.main()
