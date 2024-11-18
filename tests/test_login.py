import unittest
from authentication.login import login_form, authenticate_user, login_error_message

class TestLogin(unittest.TestCase):

    def setUp(self):
        """Set up test resources"""
        self.valid_username = 'testuser'
        self.valid_password = 'correctpassword'
        self.invalid_username = 'invaliduser'
        self.invalid_password = 'wrongpassword'

    def test_login_form_rendering(self):
        """This unit test will verify whether the login form is rendered correctly."""
        form = login_form()
        self.assertIn('<form', form)
        self.assertIn('name="username"', form)
        self.assertIn('name="password"', form)

    def test_authenticate_user_valid(self):
        """This unit test will validate the correct user credentials."""
        result = authenticate_user(self.valid_username, self.valid_password)
        self.assertTrue(result)

    def test_authenticate_user_invalid(self):
        """This unit test will validate the response for incorrect user credentials showing an error message."""
        result = authenticate_user(self.invalid_username, self.invalid_password)
        self.assertFalse(result)
        error_message = login_error_message()
        self.assertIn('Invalid username or password', error_message)

if __name__ == '__main__':
    unittest.main()
