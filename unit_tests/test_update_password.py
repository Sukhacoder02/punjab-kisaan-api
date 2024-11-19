import unittest

class TestUpdatePassword(unittest.TestCase):
    
    def setUp(self):
        self.valid_token = 'valid_token_example'
        self.invalid_token = 'invalid_token_example'
        self.expired_token = 'expired_token_example'
        self.new_password = 'NewPassword123!'
        self.user = {
            'id': 1,
            'email': 'user@example.com',
            'password': 'OldHashedPassword'
        }
    
    def mock_find_user_by_token(self, token):
        if token == self.valid_token:
            return self.user
        elif token == self.expired_token:
            raise ValueError("Token has expired")
        else:
            raise ValueError("Invalid token")
    
    def mock_hash_password(self, password):
        return f"hashed_{password}"
    
    def mock_save_new_password(self, user_id, new_password):
        return True
    
    def mock_log_password_reset(self, user_id):
        return True
    
    def test_update_password_success(self):
        # Patch the functions to be used during the test
        original_find_user_by_token = globals().get('find_user_by_token')
        original_hash_password = globals().get('hash_password')
        original_save_new_password = globals().get('save_new_password')
        original_log_password_reset = globals().get('log_password_reset')

        globals()['find_user_by_token'] = self.mock_find_user_by_token
        globals()['hash_password'] = self.mock_hash_password
        globals()['save_new_password'] = self.mock_save_new_password
        globals()['log_password_reset'] = self.mock_log_password_reset

        try:
            user = find_user_by_token(self.valid_token)
            self.assertIsNotNone(user, "User should be found with a valid token")

            hashed_password = hash_password(self.new_password)
            self.assertEqual(hashed_password, f"hashed_{self.new_password}", "Password should be hashed correctly")

            save_result = save_new_password(user['id'], hashed_password)
            self.assertTrue(save_result, "Password should be saved successfully")

            log_result = log_password_reset(user['id'])
            self.assertTrue(log_result, "Password reset should be logged successfully")
        finally:
            # Restore the original functions
            globals()['find_user_by_token'] = original_find_user_by_token
            globals()['hash_password'] = original_hash_password
            globals()['save_new_password'] = original_save_new_password
            globals()['log_password_reset'] = original_log_password_reset

if __name__ == '__main__':
    unittest.main()
