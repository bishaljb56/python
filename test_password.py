import unittest
from password_manager import PasswordManager


class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        self.password_manager = PasswordManager('password0')

    def test_get_password(self):
        self.assertEqual(self.password_manager.get_password(), 'password0')

    def test_is_correct(self):
        self.assertTrue(self.password_manager.is_correct('password0'))
        self.assertFalse(self.password_manager.is_correct('wrongpassword'))

    def test_set_password(self):
        self.password_manager.set_password('password1')
        self.assertEqual(self.password_manager.get_password(), 'password1')
        self.assertRaises(ValueError, self.password_manager.set_password, 'password0')
        self.assertRaises(ValueError, self.password_manager.set_password, 'pw2')

    def test_get_level(self):
        self.assertEqual(self.password_manager.get_level(), 0)
        self.assertEqual(self.password_manager.get_level('password1'), 0)
        self.assertEqual(self.password_manager.get_level('Pw0'), 1)
        self.assertEqual(self.password_manager.get_level('pw0!'), 2)


if __name__ == '__main__':
    unittest.main()
