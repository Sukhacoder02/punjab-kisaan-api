import unittest
from support.features import access_support_features
from authentication.login import authenticate_user

class TestSupportFeatures(unittest.TestCase):

    def setUp(self):
        self.valid_username = "testuser"
        self.valid_password = "securepassword"
        self.invalid_username = "invaliduser"
        self.invalid_password = "wrongpassword"

    def test_access_support_features(self):
        # First, we need to authenticate the user
        user_authenticated = authenticate_user(self.valid_username, self.valid_password)
        self.assertTrue(user_authenticated, "User should be authenticated with valid credentials")

        # Grant access to support features
        access_granted = access_support_features(self.valid_username)
        self.assertTrue(access_granted, "Access to support features should be granted after successful login")

        # Test access with invalid user credentials
        user_authenticated = authenticate_user(self.invalid_username, self.invalid_password)
        self.assertFalse(user_authenticated, "User should not be authenticated with invalid credentials")

        access_granted = access_support_features(self.invalid_username)
        self.assertFalse(access_granted, "Access to support features should not be granted with invalid user")

if __name__ == '__main__':
    unittest.main()
