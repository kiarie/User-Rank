import unittest
from user_rank import User


class TestUserRank(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()

    def tearDown(self) -> None:
        self.user = None

    def test_user_progress(self):
        self.assertEqual(self.user.rank, -8)
        self.assertEqual(self.user.progress, 0)
        self.user.inc_progress(-7)
        self.assertEqual(self.user.progress, 10)
        self.user.inc_progress(-8)
        self.assertEqual(self.user.progress, 13)
        self.user.inc_progress(-6)
        self.assertEqual(self.user.progress, 53)

    def test_user_ranking(self):
        self.assertEqual(self.user.rank, -8)
        self.user.inc_progress(-7)
        self.assertEqual(self.user.progress, 10)
        self.user.inc_progress(-4)
        self.assertEqual(self.user.progress, 70)  # 170 - 100
        self.assertEqual(self.user.rank, -7)

    def test_valid_ranking(self):
        self.assertEqual(self.user.rank, -8)
        self.user.set_rank(7)
        self.assertEqual(self.user.rank, -1)
        self.user.inc_progress(4)
        self.assertEqual(self.user.progress, 60)  # 170 - 100
        self.assertEqual(self.user.rank, 1) # Skips zero
        self.assertRaises(ValueError, self.user.inc_progress, 43) # aise error for invalid rank

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestUserRank)
    unittest.TextTestRunner().run(suite)
