import unittest

from birdyboard import *


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        self.birdy = Birdyboard()
        self.birdy.user = self.birdy.User("bob vila", "bob_the_builder")

        self.assertEqual("bob vila", self.birdy.user.full_name)
        self.assertEqual("bob_the_builder", self.birdy.user.screen_name)
        self.assertIsNotNone(self.birdy.user.unique_user_ID)
        self.assertIsInstance(self.birdy.user, self.birdy.User)


if __name__ == '__main__':
    unittest.main()
